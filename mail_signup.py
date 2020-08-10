import requests
from bs4 import BeautifulSoup
# response = requests.get('https://temp-mail.org/en/10minutemail')
# output = response.text

# soup = BeautifulSoup(output, 'lxml')
# result = soup.findAll("input",{"class": "emailbox-input opentip"})

# for item in result:
# 	print(item)

# import urllib3
# url = "https://temp-mail.org/en/10minutemail"
# page = urllib3.urlopen(url)
# data = page.read()
# print(data)

# import urllib3

# http = urllib3.PoolManager()
# r = http.request('get', "https://temp-mail.org/en/10minutemail")
# print(r.data)

from selenium import webdriver
path = 'chromedriver84'
driver = webdriver.Chrome(executable_path = path)
driver.get('https://www.minuteinbox.com/')
driver.implicitly_wait(10)
output = driver.page_source

soup = BeautifulSoup(output, 'lxml')
result = soup.findAll("span",{"id": "email"})

for item in result:
	print(item)
	item = str(item)
	item = item.replace('</span>','')
	item = item.replace('<span class="animace" id="email" style="font-size: 1.4em;">','')

	f = open('temp.txt','w')
	f.write(item)
	f.close()
