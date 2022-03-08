import time
import unittest
from utils import retrieve_links
from main import ProducerThread, ConsumerThread


class TestUtilMethods(unittest.TestCase):

    def test_retrieve_links(self):
        url = 'https://www.mycompany.com'
        html = '''<!DOCTYPE html>
                <html>
                <body>
                    <div id="div1">
                        <a href="/home">This is the first link</a>
                    </div>
                    <div id="div2">
                        <a href="/customers">This is the second link</a>
                    </div>
                    <div id="div3">
                        <a href="/contacts">This is the third link</a>
                    </div>
                </body>
                </html>'''

        links = retrieve_links(url, html)

        self.assertTrue(len(links) == 3)
        self.assertTrue(links[0] == 'https://www.mycompany.com/home')
        self.assertTrue(links[1] == 'https://www.mycompany.com/customers')
        self.assertTrue(links[2] == 'https://www.mycompany.com/contacts')


class TestProducerConsumerMethods(unittest.TestCase):

    def test_producer_consumer(self):
        producer_thread = ProducerThread('test_input')
        consumer_thread = ConsumerThread('test_output')
        threads = [producer_thread, consumer_thread]

        producer_thread.start()
        consumer_thread.start()

        done = False
        while not done:
            done = True
            for t in threads:
                if t.is_alive():
                    done = False
                    time.sleep(1)

        f1 = open('data/test_input')
        f2 = open('data/test_output')

        rows1 = len(f1.readlines())
        rows2 = len(f2.readlines())

        self.assertTrue(rows2 == 2 * rows1)

        f1.close()
        f2.close()


if __name__ == '__main__':
    unittest.main()