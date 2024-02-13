from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.palas.ie/")
soup = BeautifulSoup(r.content, 'lxml')

headings = soup.find_all("div",class_="film")
for h in headings:
    title = h.find("h3")
    print(title.text)