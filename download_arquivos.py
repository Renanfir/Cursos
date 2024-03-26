import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(res.raise_for_status())
playFile = open('romel.txt', 'wb')

for chunk in res.iter_content(100000):
    print(playFile.write(chunk))

playFile.close()
