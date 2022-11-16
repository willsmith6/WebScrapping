from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://cryptoslate.com/coins/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
#title = soup.title
#print(title.text)

table_rows = soup.findAll("tr")
table_cells = soup.findAll("td")
#print(table_rows[1].text)
#print(table_cells[1].text)


#rank = [0]
#name = [1]
#price = [2]
#24H% = [3]
#7D% = [4]
#30D% = [5]
#Market Cap = [6]
#24H Vol = [7]
#ATH = [8]
#%ATH = [9]

counter = 1
for x in range(5):
    name = table_cells[counter].text
    cur_price = table_cells[counter+1].text
    pcnt_cng = table_cells[counter+2].text
    price_pcnt_cng = (float(table_cells[counter+1].text.replace('$','').replace(' ','').replace(",",''))
    * (float(table_cells[counter+2].text.replace(' ','').replace('+','').replace('-','').replace('%',''))/100)
    )
    
    print(f"Name: {name}")
    print(f"Current Price: {cur_price}")
    print(f"% Change on webpage: {pcnt_cng}")
    print(f"Calculated % Change Price: ${round(price_pcnt_cng,6)}")
    print()
    counter +=10





btc = float(table_cells[2].text.replace('$','').replace(' ','').replace(",",''))
#print(btc)
eth = float(table_cells[12].text.replace('$','').replace(' ','').replace(",",''))
#print(eth)

#import keys2
accountSID = 'ACb26dfaefbb289b6b7361e7088f794bc6'
authTOKEN= '342152c2424ad98e73d5110dadedbb02'
from twilio.rest import Client

client = Client(accountSID, authTOKEN)

TwilioNumber = '+12544002405'
myCellPhone = '+18307088505'

if btc < 40000:
    print(f"Current BTC Price: ${btc}")
    btc_textmsg = client.messages.create(to=myCellPhone,from_=TwilioNumber,body='BTC dropped below $40,000')

if eth < 3000:
    print(f"Current ETH Price: ${eth}")
    eth_textmsg = client.messages.create(to=myCellPhone,from_=TwilioNumber,body='ETH dropped below $3,000')

print('BTC Status',btc_textmsg.status)
print('ETH Status',eth_textmsg.status)