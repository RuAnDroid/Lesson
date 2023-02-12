import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open("plug.csv", "a") as f:
        writer = csv.writer(f, lineterminator="\r", delimiter=";")
        writer.writerow((data['name'], data['url']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find('ul', class_='parts-page__body _parts-news')
    plugins = p1.find_all('li', class_='parts-page__item')
    for plugin in plugins:
        name = plugin.find("a").text
        url = plugin.find("a").get("href")
        data = {"name": name, "url": url}
        write_csv(data)


def main():
    url = 'https://lenta.ru/parts/news/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
