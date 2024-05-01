
from bs4 import BeautifulSoup
import requests
import sys



def fetchPage(url):
    try:
        response = requests.get(url)
        print(response.content)
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
    
    print("Movies:",end="")
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
    movieRequest = input("\n\nWhat movie would you like to find more about? Type 'Exit' to exit:\n")
    return movieRequest

def createNewURL(url,movieRequest):
    
    if movieRequest == "exit":
            sys.exit("You typed Exit. Goodbye!")
            
    movie = "-".join(movieRequest.split())
    return f"{url}/film/{movieRequest}"


    
def getPalasDetails(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"lxml")
    
    filmDetails = soup.find("section", class_="film-details")
    title = filmDetails.find("strong")
    castAndCrew = filmDetails.find("div",class_="details")
    synopsis = filmDetails.find("div",class_="synopsis").p.text
    
    print(title)
    for child in castAndCrew.children:
        print(child.text)
    print(synopsis)
    
    listofTimes = filmDetails.find("div","showtimes").ul
    for child in listofTimes.children:
        print(child.em.text)
        palasTimes = listofTimes.find("div","picktime")
        for time in palasTimes:
            print(time.text.replace("\n"," "),end="")
        print("\n")
    
url = "https://www.palas.ie/" 
webResponse = fetchPage(url)
soup = BeautifulSoup(webResponse,"lxml")
films = parseMovies(soup)
printMovies(films)

choice = getUserChoice(url)
newUrl = createNewURL(url, choice)
### unfinished
