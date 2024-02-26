import requests
from bs4 import BeautifulSoup


def pandemic():
    url = 'https://www.worldometers.info/coronavirus/'
    request = requests.get(url)

    soup = BeautifulSoup(request.text, 'html.parser')
    soup.prettify()
    total_cases = soup.find_all(class_='maincounter-number')[0].get_text().strip()
    total_deaths = soup.find_all(class_='maincounter-number')[1].get_text().strip()
    total_recovered = soup.find_all(class_='maincounter-number')[2].get_text().strip()
    return total_cases, total_deaths, total_recovered
