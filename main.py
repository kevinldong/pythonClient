import requests


url = 'http://127.0.0.1:5000/'
url01 = requests.get('http://127.0.0.1:5000/file1/')
url02 = requests.get('http://127.0.0.1:5000/file2/')
url03 = requests.get('http://127.0.0.1:5000/file3/')

with open('Unit01.png', 'wb') as a:
    a.write(url01.content)
with open('Unit02.png', 'wb') as b:
    b.write(url02.content)
with open('Unit03.png', 'wb') as c:
    c.write(url03.content)

data = open('Unit00.png', 'rb').read()
r = requests.post(url, data=data)


