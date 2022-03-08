import requests
import csv
from queue import Queue
from threading import Thread
from utils import retrieve_links

QUEUE_SIZE = 10

queue = Queue(QUEUE_SIZE)
completed = False


class RetrieveUrlContentThread(Thread):

    def __init__(self, url):
        self.url = url
        super(self.__class__, self).__init__()

    def run(self):
        global queue
        try:
            req = requests.get(self.url)
            queue.put((self.url, req.text))
        except Exception as exc:
            print("Unexpected error while fetching response for " + self.url + ":", exc)


class ProducerThread(Thread):

    def __init__(self, input_file):
        self.input_file = input_file
        super(self.__class__, self).__init__()

    def run(self):
        global queue, completed
        threads = []

        if self.input_file:
            try:
                f = open('data/' + self.input_file)
                for url in f:
                    t = RetrieveUrlContentThread(url.strip())
                    threads.append(t)
                    t.start()
                f.close()

                for t in threads:
                    t.join()
            except Exception as exc:
                print("Unexpected error while reading input file " + input_file + ":", exc)

        completed = True
        queue.put((None, None))


class ConsumerThread(Thread):

    def __init__(self, output_file):
        self.output_file = output_file
        super(self.__class__, self).__init__()

    def run(self):
        global queue, completed
        while not queue.empty() or not completed:
            url, response_html = queue.get()

            if url is not None and response_html is not None:
                try:
                    links = retrieve_links(url, response_html)
                    with open('data/' + self.output_file, 'a') as output:
                        csv.writer(output).writerow([url] + links)
                except Exception as exc:
                    print("Unexpected error while processing response for " + url + ":", exc)

            queue.task_done()


if __name__ == '__main__':

    input_file = 'input'
    output_file = 'output'

    ProducerThread(input_file).start()
    ConsumerThread(output_file).start()
