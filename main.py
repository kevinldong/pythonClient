import requests
import argparse

parser = argparse.ArgumentParser(description='uploads or downloads files from web server')
parser.add_argument('action', type=str, metavar='', help='enter your action')
parser.add_argument('filename', type=str, metavar='', help='enter the file you would like to use')
args = parser.parse_args()

action = args.action
filename = args.filename

url = 'http://127.0.0.1:5000/'
if action == 'd':
    url01 = requests.get(f'{url}/files/')
    url02 = requests.get(f'{url}/download/Unit01.png')
    url03 = requests.get(f'{url}/file3/')
    if filename == 'Unit01.png':
        with open('Unit01.png', 'wb') as a:
            a.write(url01.content)
    elif filename == 'Unit02.png':
        with open('Unit02.png', 'wb') as b:
            b.write(url02.content)
    elif filename == 'Unit03.png':
        with open('Unit03.png', 'wb') as c:
            c.write(url03.content)
    else:
        print('that is not an available file')

elif action == 'u':
    if filename == 'Unit00.png':
        data = open('Unit00.png', 'rb').read()
        r = requests.post(url, data=data)

else:
    print('that is not an available action')
