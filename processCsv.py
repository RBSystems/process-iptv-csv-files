import csv
import argparse
import requests
import json

class mydict(dict):
        def __str__(self):
            return json.dumps(self)

parser = argparse.ArgumentParser(description='Process a list of IPTV changes.')
parser.add_argument('--csvFile')

args = parser.parse_args()

with open(args.csvFile) as f:
    reader = csv.DictReader(f,delimiter='|')
    updates = list(reader)

payload = {'entries' : []}

for line in updates:
    if (len(line) > 0):
        if(line['ACTION'] == "Drop"):
            payload['entries'].append({'action':line['ACTION'],'password':line['BYU_ID']})
        elif(line['ACTION'] == "Add"):
            payload['entries'].append({'action' : line['ACTION'], 'userid' : line['NET_ID'], 'password' : line['BYU_ID'], 'name' : line['NAME'], 'location': line['BEDSPACE'] })
        else:
            continue
    else:
        continue

body = mydict(payload)
print body
url = 'http://206.174.165.241/cgi-bin/api/adddrop.cgi'
response = requests.post(url, data=body)

print response
