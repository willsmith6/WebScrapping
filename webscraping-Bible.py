import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


#https://ebible.org/asv/JHN05.htm
webpage = 'https://ebible.org/asv/JHN'

random_chapter = 1
#random_chapter = random.randint(1,21)
if random_chapter < 10:
    random_chapter = "0"+str(random_chapter)
else:
    random_chapter = str(random_chapter)
#print(random_chapter)

webpage = webpage + random_chapter + ".htm"
print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
title = soup.title



page_verses = soup.findAll("div", class_= 'main')

counter = 1
verse_list = []

for verse in page_verses:
    counter = counter+1
    #verse_list = verse.text.split(str(counter))
    #int(counter) + 1
    #verse_list = verse.text.split(str(1))
    verse_list = verse.text.split(".")
    
print(random.choice(verse_list))
#print(verse_list)

myverse = 'Chapter:' + random_chapter + ' Verse:' + random.choice(verse_list[:len(verse_list)-2])
#print(myverse)

print()


import keys2
from twilio.rest import Client


client = Client(keys2.accountSID, keys2.authTOKEN)

TwilioNumber = '+12544002405'
myCellPhone = '+18307088505'

textmsg = client.messages.create(to=myCellPhone,from_=TwilioNumber,body=myverse)
print(textmsg.status)
