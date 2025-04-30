from bs4 import BeautifulSoup
import requests
renthop = 'https://www.w3schools.com/python/default.asp'

response = requests.get(renthop)

if response.status_code != 200:
    print(f"Fetch Failed, Response: {response}")
    exit()

html = response.text
soup = BeautifulSoup(html, 'html.parser')

parags = soup.find_all('p')

print(soup.title.text)
for parag in parags:
    print(parag.text.strip())

links = soup.find_all('a')
for link in links:
    print(link.text.strip())
    print(link.get('href'))

images = soup.find_all('img')
count = 1
for image in images:
    
    src = image.get('src')
    src = f'http://www.w3schools.com{src}'
    file_name = src.split('/')[-1]
    res = requests.get(src)
    binary_data = res.content
    
    f = open(file_name, 'wb')
    f.write(binary_data)
    f.close()
    count += 1



