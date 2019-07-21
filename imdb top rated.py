from bs4 import BeautifulSoup as bs
import requests

#remove one hashtag from the start of url and run the script.

url='https://www.imdb.com/chart/top' #top rated movies
#url='https://www.imdb.com/chart/top-english-movies' #top rated english movies
#url='https://www.imdb.com/chart/toptv/'   #top rated tv shows
#url='https://www.imdb.com/india/top-rated-indian-movies' #top rated indian movies
#url='https://www.imdb.com/india/top-rated-telugu-movies' #top rated telugu movies
#url='https://www.imdb.com/india/top-rated-tamil-movies' #top rated tamil movies
#url='https://www.imdb.com/india/top-rated-malayalam-movies' #top rated malayalam movies
#url='https://www.imdb.com/chart/bottom' #lowest rated movies

response=requests.get(url)
soup=bs(response.text,"html.parser")
result=soup.find_all('td',class_="titleColumn")
rating=soup.find_all('td',class_='ratingColumn imdbRating')

final=[]
final2=[]
for r in rating:
    RatingBasedOn=r.find('strong')['title']
    rate=r.find('strong').text
    final2.append([rate,RatingBasedOn])
for r in result:
    name=r.find('a').text
    link=r.find('a')["href"]
    year=r.find('span',class_="secondaryInfo").text
    final.append([name,"https://www.imdb.com"+link,year])

for f in range(len(final)):
    final[f].append(final2[f][0])
    final[f].append(final2[f][1])


#just to save data in csv file
import csv
with open('imdb.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file, delimiter=',')
    for i in final:
        writer.writerow(i)

#better representation of scraped data using Pandas
import pandas as pd
z=pd.DataFrame(final,columns=["Movie","Link","Year","Rating","Rating Based On"])
z

