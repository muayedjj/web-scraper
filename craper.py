import requests
from bs4 import BeautifulSoup

wp_url = 'https://en.wikipedia.org/wiki/History_of_Mexico'


def get_citations_needed_count(url: str):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    sups = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')

    i = 0

    for sups in sups:
        # cits.append(cit)
        i += 1
    # print(f'The number of citations needed in this page is {i}')
    return f'The number of citations needed in this page is {i}'


# -----------------------------------------------------

def get_citations_needed_report(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = soup.find_all('a', text='citation needed')

    output = []

    for citation in citations:
        paragraph = citation.find_parents('p')[0].text
        output.append(paragraph)

    rep = '\n'.join(output)

    return rep.strip()


# -----------------------------------------------------
if __name__ == "__main__":
    print(get_citations_needed_report(wp_url))
