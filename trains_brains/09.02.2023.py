import requests
from bs4 import BeautifulSoup
from parcers import Parsers


def main():
    pars = Parsers("https://www.ixbt.com/live/index/news/", "new.txt")
    pars.run()


if __name__ == '__main__':
    main()
