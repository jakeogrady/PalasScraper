from bs4 import BeautifulSoup
import requests
url = "https://www.palas.ie/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')

def displayFilms():
    list = soup.find_all("div", class_="film")
    for film in list:
        str = ""
        title = film.find("h3").find("a")
        
        timeSlots = film.find("div",class_="times")
        times = timeSlots.find_all("a")
        if times:
            str += title.text+":"
            for time in times:
                str+= " " + time.text
            print(str)
        
todaysMovies = displayFilms()
