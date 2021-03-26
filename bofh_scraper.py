#!/usr/bin/env python
## EXECUTION EXAMPLE: python3 ./bofh_scraper.py ##
import requests
from bs4 import BeautifulSoup
import re
import random

# Creating the empty arrays #
first = []
second = []
third = []
fourth = []
excuse = []

# Looking for the table #
r = requests.get('http://bofh.bjash.com/ExcuseBoard.html', verify=False)
soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find_all('table')[0]
# Locate each column of table #
firstColumn = re.findall(r'\s+[a-zA-Z-]+<br\/>', str(table.find_all('td')[0].contents))
secondColumn = re.findall(r'\s+[a-zA-Z-]+<br\/>', str(table.find_all('td')[1].contents))
thirdColumn = re.findall(r'\s+[a-zA-Z-]+<br\/>', str(table.find_all('td')[2].contents))
fourthColumn = re.findall(r'\s+[a-zA-Z-]+<br\/>', str(table.find_all('td')[3].contents))

# Perform some initial stripping #
for x in firstColumn:
    first.append((re.sub(r'<br\/>', '', x.strip("\r"))))

for x in secondColumn:
    second.append((re.sub(r'<br\/>', '', x.strip("\r"))))

for x in thirdColumn:
    third.append((re.sub(r'<br\/>', '', x.strip("\r"))))

for x in fourthColumn:
    fourth.append((re.sub(r'<br\/>', '', x.strip("\r"))))

# Define lists #
for i in first:
	o1 = random.choice(first)
	o2 = random.choice(second)
	o3 = random.choice(third)
	o4 = random.choice(fourth)
# Do some formatting of each line, and create final list of excuses #	
	tricky = o1.lstrip() + " " + o2.lstrip() + " " + o3.lstrip() + " " + o4.lstrip()
	excuse.append(tricky)

# Define snarky output #	
print("Please provide following excuse to user:",random.choice(excuse))