from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.palas.ie/")
soup = BeautifulSoup(r.content, 'lxml')
listOfMovies = []
headings = soup.find_all("div",class_="film")
for h in headings:
    movieInfo = {}
    title = h.find("h3")
    time = h.find("div",class_="times")
    times = time.find("a")
    if times:
         print(f'{title.text}: {times.text}')
         movieInfo['title'] = title.text
         movieInfo['times'] = times.text
         listOfMovies.append(movieInfo)
    
