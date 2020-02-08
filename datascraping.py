from bs4 import BeautifulSoup
import requests
import pandas as pd


def printData(url):
    import bs4
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup

    #testing url
    my_url = url;

    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Below is in charge of finding: Title
    #Getting the title - stored in realTitle
    titleClass = page_soup.findAll("h1",{"class":"mop-ratings-wrap__title mop-ratings-wrap__title--top"})
    realTitle = titleClass[0].text;
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Below is in charge of finding: Rating
    #Getting the rating - stored in rating
    ratingArray = page_soup.findAll("div",{"class":"meta-value"});
    rating = ratingArray[0].text;

    #Array that gets most of the data
    genreArray = page_soup.findAll("div",{"class":"meta-value"})
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Below is in charge of finding: genre
    #Getting the genre - store in genreString
    genreString = "";
    for item in (genreArray[1].findAll('a')):
        genreString += item.text
        if (item != genreArray[1].findAll('a')[-1]):
            genreString += ", "

    directedBy = "";   
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Below is in charge of finding: RunTime and Studio
#Three Different Cases found so far
#Getting the runtime - store in runTime
#Getting the Studio - store in studio
#Last Character in the length of runTime should always end with a 's' so here I will change my program to search if there is a 's' at the runTime string if there is no then I know that there is some mix up
    if (len(genreArray) == 9):
        possibleRunTime = genreArray[7].text.strip();
        isNormal = False
        lastCharInPossibleRunTime = possibleRunTime[len(possibleRunTime)-1]
        if (lastCharInPossibleRunTime == 's'):
            isNormal = True
        if (isNormal == True):
            runTime = genreArray[7].text.strip()
            if(len(genreArray[8]) != 1):
                studio = "N/A"
            else:
                studio = genreArray[8].text.strip();
        else: #Else switch the index around
            runTime = genreArray[8].text.strip()
            if(len(genreArray[7]) != 1):
                studio = "N/A"
            else:
                studio = genreArray[7].text.strip();

    if (len(genreArray) == 8):
        possibleRunTime = genreArray[6].text.strip();
        isNormal = False
        lastCharInPossibleRunTime = possibleRunTime[len(possibleRunTime)-1]
        if (lastCharInPossibleRunTime == 's'):
            isNormal = True
        if (isNormal == True):
            runTime = genreArray[6].text.strip()
            if(len(genreArray[7]) != 1):
                studio = "N/A"
            else:
                studio = genreArray[7].text.strip();
        else: #Else switch the index around
            runTime = genreArray[7].text.strip()
            if(len(genreArray[6]) != 1):
                studio = "N/A"
            else:
                studio = genreArray[6].text.strip();

    if (len(genreArray) == 7):
        possibleRunTime = genreArray[5].text.strip();
        isNormal = False
        lastCharInPossibleRunTime = possibleRunTime[len(possibleRunTime)-1]
        if (lastCharInPossibleRunTime == 's'):
            isNormal = True
        if (isNormal == True):
            runTime = genreArray[5].text.strip()
            if(len(genreArray[6]) != 1):
                studio = "N/A"
            else:
                studio = genreArray[6].text.strip();
        else: #Else switch the index around
            runTime = genreArray[6].text.strip()
            if(len(genreArray[5]) != 1):
                studio = "N/A"
            else:
                studio = genreArray[5].text.strip();
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Below is in charge of finding: directedBy
#Getting the directors - stored in directedBy
    directorArray = genreArray[2].findAll("a")
    for item in directorArray:
        directedBy += item.text.strip()
        if (item != directorArray[-1]):
            directedBy += ", "
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Below is in charge of finding: sypnosis
    #Getting the synopsis - stored in realSynopsis
    synopsisArray = page_soup.findAll("div",{"id":"movieSynopsis"})
    realSynopsis = synopsisArray[0].text.strip().replace('\'',"")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Below is in charge of finding: tomatometer & count and tomatoMeter & tomatoCount
    #Getting the tomatometer & count - stored in tomatoMeter & tomatoCount
    tomatoMeterArray = page_soup.findAll("span",{"class":"mop-ratings-wrap__percentage"})
    tomatoMeter = tomatoMeterArray[0].text.strip()
    tomatoCountArray = page_soup.findAll("small",{"class","mop-ratings-wrap__text--small"})
    tomatoCount = tomatoCountArray[0].text.strip()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Below is in charge of finding: audience store & count audienceScore & audienceCount
    #Getting the audience store & count - stored in audienceScore & audienceCount
    audienceScore = tomatoMeterArray[1].text.strip()
    audienceCountArray = page_soup.findAll("strong",{"class","mop-ratings-wrap__text--small"})
    audienceCountUnfiltered = audienceCountArray[1].text.strip()
    audienceCount = "";
    for item in audienceCountUnfiltered:
        if (item.isnumeric() == True):
            audienceCount += item;
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Below is in charge of finding: critics concensus
    #Getting the critics concensus - stored in criticsConcensus
    criticArray = page_soup.findAll("p",{"class":"mop-ratings-wrap__text mop-ratings-wrap__text--concensus"})
    criticsConcensus = "";
    if (len(criticArray) == 0):
        criticsConcensus = "N/A";
    else:
        criticsConcensus = criticArray[0].text.strip()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Below is in charge of finding: Top 3 cast members
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
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#This marks the end of the function - created by Trung Bui, Scraping Information from Rotten Tomatoes movies        

#Checking the attributes
    # print("Title:             " + realTitle)
    # print("Critics Concensus: " + criticsConcensus)
    # print("Tomato Meter:      " + tomatoMeter)
    # print("Tomato Count:      " + tomatoCount)
    # print("Audience Score:    " + audienceScore)
    # print("Audience Count:    " + audienceCount)
    # print("Synopsis:         " + realSynopsis)
    # print("Rating:           " + rating)
    # print("Genre:            " + genreString)
    # print("Directed By:      " + directedBy)
    # print("Studio:           " + studio)
    # print("Run Time:         " + runTime)
    # print("Top 3 Casts:      " + cast)
    return [realTitle, criticsConcensus, tomatoMeter, tomatoCount, 
            audienceScore, audienceCount, realSynopsis, rating, genreString, 
            directedBy, studio, runTime, cast]