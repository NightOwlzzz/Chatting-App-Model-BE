from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

def recommend(emotion):
    if(emotion == "sad"):
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
  
    elif(emotion == "angry" or emotion == "alone" or emotion == "lost" or emotion == "independent" or emotion == "belittled"):
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
  
    elif(emotion == "powerless" or emotion == "codependent" or emotion == "average"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
    elif(emotion == "fearful" or emotion == "demoralized" or emotion == "fearless" or emotion == "derailed" or emotion == "anxious"):
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
  
    elif(emotion == "esteemed" or emotion == "entitled"):
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
  
    elif(emotion == "surprise"):
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
  
    elif(emotion == "embarrassed" or emotion == "bored" or emotion == "burdened" or emotion == "happy" or emotion == "ecstatic"):
        urlhere = 'https://www.imdb.com/search/title/?genres=comedy&title_type=feature&sort=moviemeter, asc'
    
    elif(emotion == "loved" or emotion == "attached" or emotion == "lustful" or emotion == "singled out" or emotion == "hated" or emotion == "attracted"):
        urlhere = 'https://www.imdb.com/search/title/?genres=romance&title_type=feature&sort=moviemeter, asc'
    
    elif(emotion == "focused" or emotion == "obsessed"):
        urlhere = 'https://www.imdb.com/search/title/?genres=mystery&title_type=feature&sort=moviemeter, asc'
    
    elif(emotion == "free" or emotion == "adequate" or emotion == "safe" or emotion == "happy"):
        urlhere = 'https://www.imdb.com/search/title/?genres=adventure&title_type=feature&sort=moviemeter, asc'
    
    elif(emotion == "apathetic"):
        urlhere = 'https://www.imdb.com/search/title/?genres=fantasy&title_type=feature&sort=moviemeter, asc'
    
    elif(emotion == "cheated"):
        urlhere = 'https://www.imdb.com/search/title/?genres=comedy,romance&title_type=feature&sort=moviemeter, asc'
        
    elif(emotion == "adequate"):
        urlhere = 'https://www.imdb.com/search/title/?genres=comedy,action&title_type=feature&sort=moviemeter, asc'
    
    else:
        urlhere = 'https://www.imdb.com/search/title/?genres=comedy&title_type=feature&sort=moviemeter, asc'
 
    response = HTTP.get(urlhere)
    data = response.text
  
    soup = SOUP(data, "html.parser")

    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    return title
  
def recommendMovies(emotion):
    movies = []
    a = recommend(emotion)
    count = 0
    for i in a:
        tmp = str(i).split('>')
        if(len(tmp) == 3):
            movies.append(tmp[1][:-3])
            count+=1

        if(count >= 10):
            break
    return movies