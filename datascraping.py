import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#testing url
my_url = "https://www.rottentomatoes.com/m/bad_boys_for_life";

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

#Getting the title - stored in realTitle
titleClass = page_soup.findAll("h1",{"class":"mop-ratings-wrap__title mop-ratings-wrap__title--top"})
realTitle = titleClass[0].text;

#Getting the rating - stored in rating
ratingArray = page_soup.findAll("div",{"class":"meta-value"});
rating = ratingArray[0].text;

#Array that gets most of the data
genreArray = page_soup.findAll("div",{"class":"meta-value"})

#Getting the genre - store in genreString
genreString = "";
for item in (genreArray[1].findAll('a')):
    genreString += item.text
    if (item != genreArray[1].findAll('a')[-1]):
        genreString += ", "

#Special Case of discrepancy    
if (len(genreArray) == 8):
    #Getting the runtime - store in runTime
    runTime = genreArray[6].text.strip()

    #Getting the Studio - store in studio
    studio = genreArray[7].text.strip();

    #Getting the directors - stored in directedBy
    directorArray = genreArray[2].findAll("a")
    directedBy = ""
    for item in directorArray:
        directedBy += item.text.strip()
        if (item != directorArray[-1]):
            directedBy += ", "

if (len(genreArray) == 7):
    #Getting the runtime - store in runTime
    runTime = genreArray[5].text.strip()

    #Getting the Studio - store in studio
    studio = genreArray[6].text.strip();

    #Getting the directors - stored in directedBy
    directorArray = genreArray[2].findAll("a")
    directedBy = ""
    for item in directorArray:
        directedBy += item.text.strip()
        if (item != directorArray[-1]):
            directedBy += ", " 
            
#Getting the synopsis - stored in realSynopsis
synopsisArray = page_soup.findAll("div",{"id":"movieSynopsis"})
realSynopsis = synopsisArray[0].text.strip().replace('\'',"")

#Getting the tomatometer & count - stored in tomatoMeter & tomatoCount
tomatoMeterArray = page_soup.findAll("span",{"class":"mop-ratings-wrap__percentage"})
tomatoMeter = tomatoMeterArray[0].text.strip()
tomatoCountArray = page_soup.findAll("small",{"class","mop-ratings-wrap__text--small"})
tomatoCount = tomatoCountArray[0].text.strip()

#Getting the audience store & count - stored in audienceScore & audienceCount
audienceScore = tomatoMeterArray[1].text.strip()
audienceCountArray = page_soup.findAll("strong",{"class","mop-ratings-wrap__text--small"})
audienceCountUnfiltered = audienceCountArray[1].text.strip()
audienceCount = "";
for item in audienceCountUnfiltered:
    if (item.isnumeric() == True):
        audienceCount += item;
        
#Getting the critics concensus - stored in criticsConcensus
criticArray = page_soup.findAll("p",{"class":"mop-ratings-wrap__text mop-ratings-wrap__text--concensus"})
criticsConcensus = criticArray[0].text.strip()

#Getting the top 3 cast members - stored in cast
castHTMLArray = page_soup.findAll("div",{"class":"castSection"})
castMiniArray = castHTMLArray[0].findAll("span")
x = 0;
cast = ""; 
while (x != 6):
    cast += castMiniArray[x].text.strip()
    if (castMiniArray[x] != castMiniArray[4]):
        cast += ", "
    x = x + 2

#Checking the attributes
print("Title:             " + realTitle)
print("Critics Concensus: " + criticsConcensus)
print("Tomato Meter:      " + tomatoMeter)
print("Tomato Count:      " + tomatoCount)
print("Audience Score:    " + audienceScore)
print("Audience Count:    " + audienceCount)
print("Synopsis:         " + realSynopsis)
print("Rating:           " + rating)
print("Genre:            " + genreString)
print("Directed By:      " + directedBy)
print("Studio:           " + studio)
print("Run Time:         " + runTime)
print("Top 3 Casts:      " + cast)

    
     