import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.sheriff.org/apps/arrest/results.cfm?lname=smith&fname='
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
print soup.prettify()
