import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


url = 'http://py4e-data.dr-chuck.net/comments_1998647.xml'
with urllib.request.urlopen(url) as response:
    data = response.read()

with open('comments.xml', 'wb') as f:
    f.write(data)
# print("XML Data:", data.decode('utf-8')) 

root = ET.fromstring(data)

# print("Root Element:", root)

lst = root.findall('comments/comment')

math = 0 

for comment in lst:
    count = comment.find('count').text
    convert = int(count)
    math = math + convert

print('Total Sum', math)


        

        
