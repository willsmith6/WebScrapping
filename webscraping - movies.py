from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

url = 'https://boxofficemojo.com/year/2022/'

# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

#print tables

td = soup.findAll('td')
movie_rows = soup.findAll('tr')

rank = td[0].text
name = td[1].text
gross = td[5].text
theaters = td[6].text
total_gross = td[7].text
release_date = td[8].text
dist = td[9].text

'''counter = 0
for i in range(5):
    print ('rank: ', td[counter].text)
    print ('relase: ', td[counter+1].text)
    print ('total gross: ', td[counter+5].text)
    print ('avg rev per theater: $', round(float(td[counter+5].text.replace('$','').replace(',',''))
                                        /float(td[counter+6].text.replace(',',''))))
    print ('distributor: ', td[counter+9].text)
    print()
    counter += 11'''


list_counter = 1
movie_list = []

#print(movie_rows)
for x in range(1,6):
    td = movie_rows[x].findAll('td')
    print(td[1].text)
    