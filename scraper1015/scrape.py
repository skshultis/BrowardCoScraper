import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.sheriff.org/apps/arrest/results.cfm?lname=smith&fname='
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class': 'datagrid'})

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        text = cell.text.replace('M&nsbp', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

    print list_of_rows
