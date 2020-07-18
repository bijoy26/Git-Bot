#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import time

print('hi all')
url='https://www.timeanddate.com/worldclock/'

response = requests.get(url)

# print(response.text)

#f = open("response_unformatted.txt", "w")
#f.write(response.text)
#f.close()

print('mid all')


soup = BeautifulSoup(response.text,'html5lib')
#soup_string = str(soup)
#print(soup)

#f = open("response_formatted.txt", "w")
#f.write(soup_string)
#f.close()


Noti = soup.find(id='c73sec')
print(Noti.text)
print('bye all')
x=50
while x>=0:
    soup = BeautifulSoup(response.text,'html5lib')
    Noti = soup.find(id='c73sec')
    print(Noti.text)
    x = x-1
    time.sleep(1)
#Price = soup.find(class='f4 text-normal mb-2')
#printf(Price)
