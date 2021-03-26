import requests
from bs4 import BeautifulSoup
import re
import random
import argparse
import json
import datetime 
import time

###teting url / token:
    #url = 'http://50.116.36.196:8088/services/collector/event'
    #token = '4cdcbe12-0eaa-4e8e-aad6-ba390becdcc8'

#creating inputs for destination URL, token, port
parser = argparse.ArgumentParser()

parser.add_argument('-u', required=True, help="Destination URL with port. ex: http://you.splunk:8088/services/collector/event ")
parser.add_argument('-t', required=True, help="Destination Token Value")

args = parser.parse_args()

du = args.u
dt = args.t

#create time variable
#string_date = "2016-11-03"
dte =  datetime.datetime.utcnow()

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

# Do some formatting of each line, and create final event #    
    tricky = o1.lstrip() + " " + o2.lstrip() + " " + o3.lstrip() + " " + o4.lstrip()
    excuse.append(tricky)

# Example of json for ref: {"date": TIMESTAMP, "rca": "Temporary Loading Desynchronisation Error"}

for excuse in excuse:
    data = json.dumps({
        "event":  {
        	"time": dte,
            "excuse": excuse
        } 
    }, default=str)
    headers = {
        'Authorization': 'Splunk ' + dt,
        'Content-Type': 'application/json'
    }
    r = requests.post(du, headers=headers, data=data, verify=False)