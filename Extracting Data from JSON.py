import json
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
html = urlopen(url, context=ctx).read()

raw_data = html.decode()

data = json.loads(raw_data)

math = 0
try:
    data = json.loads(raw_data)
    comments = data.get('comments', [])  # Get the list of comments, or an empty list if 'comments' key doesn't exist
    for comment in comments:
        count = comment.get('count')  # Get the 'count' value for each comment
        if count is not None:
            convert = int(count)
            math = math + convert
        else:
            print("No 'count' key found in this comment:", comment)
except json.decoder.JSONDecodeError:
    print("Error")

print(math)