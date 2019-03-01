import json
from pprint import pprint
import re
import os
import urllib
import requests

n = 0

with open('sacci.org.za.json', 'r') as jf:
    json_data = json.load(jf)
url_list = list()
pdf_list = list()
for x in json_data[1]['url']:
    url_list.append(json_data[1]['url'][n])
    n += 1
#same function as for statment upper => url_list = [x for x  in json_data[1]['url']

n = 0

for n in range(len(url_list)):
    pdf_filename = os.path.join('./pdf/', 'my_pdf' + str(n) + '.pdf')
    if '.pdf' not in url_list[n]:
        print(url_list[n] + "  it's not a pdf File")

    else:
        print(url_list[n] + '  Found a pdf File!!@@')
        pdf_list.append(url_list[n])
        urllib.request.urlretrieve(url_list[n], pdf_filename)

    n += 1
print("\n\n\n")
pprint(pdf_list)









"""
    json_str = json.dumps(json_data)
    print(json_str)
    json_str_list = [json_str.split('"')]# for data in check.findall(json_str)]
#print(json_str)
print(json_str_list)

for i in range(0,len(json_str_list)):
    #if re.match("pdf'$", json_str_list[i]):
        print(json_str_list[i])
"""


"""check : re.compile(".pdf$")
for n in range(0,len(json_data)):
    print(json_data["url"][n])
    n += 1

    #pprint(json_data)
    check = re.compile('.pdf$')

    ''.join(json_data[1])

print(json_data[1])

for pdf in json_data[1]:
    print(check.search(json_data[1]))
    #json_url = json_data["url"]
    pprint("\n")


    #print(json_url)
"""