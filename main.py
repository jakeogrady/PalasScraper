
from bs4 import BeautifulSoup
import requests
import sys



def fetchPage(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Success",end="")
        else:
            print(f"Page not found {url}")
            sys.exit(1)
        return response.content
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        sys.exit(1)

 # this gets the list of films on today
def parseMovies(soup):
    films = soup.find_all("div",class_="film")
    if not films:
        print("Error: No films found")
        sys.exit(1)
    return films

def printMovies(films):
    for film in films:
        movieName = film.h3.text
        movieTimes = film.find_all("div", class_="times")
        
        ## if there is no times left for this film, skip to next film
        if not movieTimes[0].text:
            continue
        
        print(f'\n{movieName}',end="")
        for time in movieTimes:
            print(time.text,end=" ")
        print("\n")
            
def getUserChoice(url):
    movieRequest = input("What movie would you like to find more about? Type 'Exit' to exit:\n")
    return movieRequest

def createNewURL(url,movieRequest):
    
    if movieRequest == "exit":
            sys.exit("You typed Exit. Goodbye!")
            
    movie = "-".join(movieRequest.split())
    return f"{url}/film/{movieRequest}"


    
def getPalasDetails(soup):
    castAndCrew = soup.find("div",class_="details")
    synopsis = soup.find("div",class_="synopsis").p.text
    for child in castAndCrew.children:
        print(child.text)
        
    print(f"\nSynopsis:\n{synopsis}")
    
    
url = "https://www.palas.ie" 
webResponse = fetchPage(url)
soup = BeautifulSoup(webResponse,"lxml")
films = parseMovies(soup)
printMovies(films)

choice = getUserChoice(url)
newUrl = createNewURL(url, choice)
webResponse = fetchPage(newUrl)
movieSoup = BeautifulSoup(webResponse, "lxml")
getPalasDetails(movieSoup)
