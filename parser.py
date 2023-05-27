import subprocess

name_lib = ['BeautifulSoup4', 'requests']

def install(name):
    subprocess.call(['pip', 'install', name])

for item in name_lib:
    install(item)

from bs4 import BeautifulSoup
import requests
import lxml

url = "https://www.fontanka.ru/24hours.html/"

headers = {
    "Accept:" "*/*",
    "user-agent:" "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
}

req = requests.get(url)
src = req.text
soup = BeautifulSoup(src, "lxml")

news = soup.find_all("a", class_="IDe3")

with open("news.txt", "w", encoding="utf-8") as file:

    for item in news:
        file.write("\n\n")
        if item.get("href")[0] == 'h':
            file.write(f'{item.text} : {item.get("href")}')
        elif item.get("href")[0] == '/':
            file.write(f'{item.text} : https://www.fontanka.ru/{item.get("href")}')

print("Новости с фантанки.ру успешно сохранены в файле news.txt в директории с этим же файлом")
input()
