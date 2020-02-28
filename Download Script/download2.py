from bs4 import BeautifulSoup
import requests
import pandas as pd
import random as rd


j = 0
err_list = []
df = pd.DataFrame(columns = ["dataIndex", "realTitle", "criticsConcensus", "tomatoMeter", "tomatoCount", 
            "audienceScore", "audienceCount", "realSynopsis", "rating", "genreString", 
            "directedBy", "studio", "runTime", "cast"])

data = pd.read_csv("movie_data.csv", error_bad_lines=False, dtype='unicode')
for i in range(0, 500):
        try:
            fixed = fixNormal(data.at[i, "title"])
            movie_data = printData("https://www.rottentomatoes.com/m/" + fixed)
            print("Success at fixNormal at new title: " + str(i))
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
            df.at[j, "dataIndex"] = i
            j += 1
        except:
            try:
                fixed = fixWithoutThe(data.at[i, "title"])
                movie_data = printData("https://www.rottentomatoes.com/m/" + fixed)
                print("Success at fixWithoutThe at new title: " + str(i))
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
                df.at[j, "dataIndex"] = i
                j += 1
            except:
                try:
                    fixed = fixNormal(data.at[i, "title"])
                    movie_data = printData("https://www.rottentomatoes.com/m/" + fixed + "_" + data.at[i, "Year"])
                    print("Success at fixNormal with new title and years: " + str(i))
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
                    df.at[j, "dataIndex"] = i
                    j += 1
                except:
                    try:
                        fixed = fixNormal(data.at[i, "original_title"])
                        movie_data = printData("https://www.rottentomatoes.com/m/" + fixed)
                        print("Success at fixNormal with Original title: " + str(i))
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
                        df.at[j, "dataIndex"] = i
                        j += 1
                    except:
                        try:
                            fixed = fixWithoutA(data.at[i, "title"])
                            movie_data = printData("https://www.rottentomatoes.com/m/" + fixed)
                            print("Success at fixWithoutA: " + str(i))
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
                            df.at[j, "dataIndex"] = i
                            j += 1
                        except:
                            err_list.append(i)
                            print("Failure: " + str(i) + (" https://www.rottentomatoes.com/m/" + fixed))
                            pass

with open("errors" + str(df.at[len(df) - 1, "dataIndex"]) + ".txt", "w") as output:
    output.write(str(str(err_list).encode('utf8')))


df.to_csv("data-" + str(df.at[len(df) - 1, "dataIndex"]) + ".csv")
