import requests
from bs4 import BeautifulSoup

wp_url = 'https://en.wikipedia.org/wiki/History_of_Mexico'


def get_citations_needed_count(url: str):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    jobs_cards = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')

    cits = []
    i = 0

    for cit in jobs_cards:
        cits.append(cit)
        i += 1
    print(f'The number of citations needed in this page is {i}')


get_citations_needed_count(wp_url)

