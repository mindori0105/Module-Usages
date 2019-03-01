import requests
from bs4 import BeautifulSoup
import urllib
import re
import shutil
import csv
from PIL import Image
import profile
import os




URL = 'http://news.naver.com'
response = requests.get(url=URL)
print(response.status_code)
n = 1
soup = BeautifulSoup(response.text, 'html.parser')
for link  in soup.findAll('img', attrs={'src': re.compile("^http://")}):
    image_url = link.get('src')

    response = requests.get(image_url, stream =True)
    image_filename = os.path.join('./news/', 'my_img'+ str(n) +'.jpg')
    print(image_filename,image_url)
    urllib.request.urlretrieve(image_url, image_filename)
    n += 1