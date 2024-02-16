from bs4 import BeautifulSoup
import requests
url = "https://www.palas.ie/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')


list = soup.find_all("div", class_="film")

for film in list:
    str = ""
    title = film.find("h3").find("a")
    str += title.text+":"
    timeSlots = film.find("div",class_="times")
    times = timeSlots.find_all("a")
    for time in times:
        str+= " " + time.text
    print(str)