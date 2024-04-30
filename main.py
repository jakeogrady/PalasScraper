from bs4 import BeautifulSoup
from datetime import date
import requests


url = "https://www.palas.ie/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
today = date.today()


div = soup.find("div", class_="tab active loaded")
films = div.find_all("div",class_="film")
# this gets the list of films on today

print(f'Movies for {today}:',end="")
for film in films:
    movieName = film.h3.a
    movieTimes = film.find_all("div", class_="times")
    
    if not movieTimes[0].text:
        continue
    
    print(f'\n{movieName.text}',end="")
    for time in movieTimes:
        print(time.text+" ")