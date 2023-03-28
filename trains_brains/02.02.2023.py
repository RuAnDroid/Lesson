# import csv
#
# with open('data.csv', 'r', encoding="utf-8") as r_file:
#     file_reader = csv.reader(r_file, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {','.join(row)}")
#         else:
#             print(f"     {row[0]} - {row[1]}. Родился в {row[2]}  году.")
#         count += 1
#     print(f"Всего в файле {count} строки")

import csv

# with open('data.csv', 'r', encoding="utf-8") as r_file:
#     field_names =['Имя','Профессия','Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=";", fieldnames=field_names)
#     count = 0
#     for row in file_reader:
#         print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"    {row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']}  году.")
#         count += 1
#     print(f"Всего в файле {count} строки")

#
# with open('student.csv', mode='w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Жека", "9", "15"])
#     writer.writerow(["Санёк", "5", "12"])
#     writer.writerow(["Машуня", "11", "18"])
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
#
# with open("data_sw.csv", mode="w") as f:
#     writer = csv.writer(f, delimiter=";",lineterminator="\r" )
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open("data_sw.csv") as f:
#     print(f.read())
#
# with open("stud.csv", mode="w") as f:
#     names = ["Имя","Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=";",lineterminator="\r",fieldnames = names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Саша","Возраст":"6"})
#     file_writer.writerow({"Имя": "Маша", "Возраст": "15"})
#     file_writer.writerow({"Имя": "Вова", "Возраст": "14"})


# data = [{
#  'hostname': 'sw1',
#  'location': 'London',
#  'model': '3750',
#  'vendor': 'Cisco'
# }, {
#  'hostname': 'sw2',
#  'location': 'Liverpool',
#  'model': '3850',
#  'vendor': 'Cisco'
# }, {
#  'hostname': 'sw3',
#  'location': 'Liverpool',
#  'model': '3650',
#  'vendor': 'Cisco'
# }, {
#  'hostname': 'sw4',
#  'location': 'London',
#  'model': '3650',
#  'vendor': 'Cisco'
# }]
# with open("dictwriter.csv", 'w') as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

from bs4 import BeautifulSoup

import re
# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois").text.strip()
#     if "Copywriter" in whois:
#         return tag
#     return None

# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.search(pattern, s).group()
#     res = re.findall(pattern,s)
#     print(res)
#
#
# f = open('head.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
# # print(salary)
# for i in salary:
#     get_salary(i.text)

# copywriter = []
# row = soup.find_all('div', class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)
# row = soup.find('div', class_="name").text
# row = soup.find_all('div', class_="name")
# print(row)
# for r in row:
#     print(r.text)
# row = soup.find_all('div', class_="row")[1].find("div", class_="links")
# print(row)
# row = soup.find_all("div", {"data-set": "salary"})
# print(row)
# row = soup.find("div", string="Alena").parent.parent
# row = soup.find("div", string="Alena").find_parent(class_='row')
# print(row)
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)

# import requests

# r = requests.get("https://ru.wordpress.org/")
# print(r.headers['Content-Type'])
# print(r.content)
# print(r.text)
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r"\D+", '', s)
#     return res
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[3]
#     plugins = p1.find_all('article')
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         url = plugin.find("h3").find("a").get("href")  # ["href"]
#         rating = plugin.find("span", class_="rating-count").find('a').text
#         r = refined(rating)
#         data = {"name": name, "url": url, "rating": r}
#         write_csv(data)
#
#     # return len(plugins)
#
#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

import requests
from bs4 import BeautifulSoup
import re
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def refine_cy(s):
    return s.split()[-1]


def refine_snippet(s):
    return re.sub(r"\\U","",s)


def write_csv(data):
    with open("plugins1.csv", "a") as f:
        writer = csv.writer(f, lineterminator="\r", delimiter=";")
        writer.writerow((data['name'], data['url'], data['snippet'], data['cy']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all("article", class_="plugin-card")
    for el in elements:
        try:
            name = el.find("h3").text
        except ValueError:
            name = ""
        try:
            url = el.find("h3").find("a").get("href")
        except ValueError:
            url = ""
        try:
            snippet = el.find("div", class_="entry-excerpt").text.strip()
            snippet1 = refine_snippet(snippet)
        except ValueError:
            snippet1 = ""
        try:
            c = el.find("span", class_="tested-with").text.strip()
            cy = refine_cy(c)
        except ValueError:
            cy = ""

        data = {
            'name': name,
            'url': url,
            'snippet': snippet,
            'cy': cy
        }
        write_csv(data)


def main():
    for i in range(0, 25):
        url = "https://ru.wordpress.org/plugins/browse/blocks/page/1/"
        get_data(get_html(url))


if __name__ == '__main__':
    main()
