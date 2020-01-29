from bs4 import BeautifulSoup
import requests
import pandas as pd

df = pd.DataFrame(columns = ["realTitle", "criticsConcensus", "tomatoMeter", "tomatoCount", 
            "audienceScore", "audienceCount", "realSynopsis", "rating", "genreString", 
            "directedBy", "studio", "runTime", "cast"])

data = pd.read_csv("movies_metadata.csv")

j = 0
err_list = []
for i in range(0, 1000): # CHANGE THIS
    #print("https://www.rottentomatoes.com/m/" + data.at[i, "original_title"].lower().replace(" ", "_"))
    try:
        movie_data = printData("https://www.rottentomatoes.com/m/" + data.at[i, "original_title"].lower().replace(" ", "_"))
        df.at[j, "realTitle"] = movie_data[0]
        df.at[j, "criticsConcensus"] = movie_data[1]
        df.at[j, "tomatoMeter"] = movie_data[2]
        df.at[j, "tomatoCount"] = movie_data[3]
        df.at[j, "audienceScore"] = movie_data[4]
        df.at[j, "audienceCount"] = movie_data[5]
        df.at[j, "realSynopsis"] = movie_data[6]
        df.at[j, "rating"] = movie_data[7]
        df.at[j, "genreString"] = movie_data[8]
        df.at[j, "directedBy"] = movie_data[9]
        df.at[j, "studio"] = movie_data[10]
        df.at[j, "runTime"] = movie_data[11]
        df.at[j, "cast"] = movie_data[12]
        j += 1
        # print(printData("https://www.rottentomatoes.com/m/" + data.at[i, "original_title"].lower().replace(" ", "_")))
    except:
        err_list.append(data.at[i, "original_title"])
        pass

with open("errors.txt", "w") as output:
    output.write(str(err_list))

df.to_csv("data.csv")