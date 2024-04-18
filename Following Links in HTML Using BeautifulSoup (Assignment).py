

import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')

for count_page in range(7):

    tag = tags[17]
    
    split = tag.decode().split('"')
    url_t = split[1]
   
    try:
        response = urllib.request.urlopen(url_t)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        #print("Successfully opened Url:", url_t)
        name_split = tag.decode().split('>')
        name_str = str(name_split[1])
        name = name_str.split('<')
        tags = soup('a')
    except:
        print("Failed to Open Url:", url_t)
    
print('The Final Name is:', name[0])


