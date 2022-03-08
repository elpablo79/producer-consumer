import bs4
from urllib.parse import urljoin


def retrieve_links(url, response_body):
    links = bs4.BeautifulSoup(response_body, 'html.parser').select('a')
    if links:
        return [urljoin(url, e['href'])
                for e in links if e.get('href')
                and not e['href'].startswith(u'javascript')
                and not e['href'].strip() == u'#']
    return []
