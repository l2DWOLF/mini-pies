import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

print(soup.title.text)
movies_li = soup.select('.ipc-metadata-list li')
for movie_li in movies_li:
    title = movie_li.select_one('.ipc-title__text').text
    meta = movie_li.select('.cli-title-metadata-item')
    rating = movie_li.select('.ipc-rating-star--rating')
    votes = movie_li.select('.ipc-rating-star--voteCount')
    descrip = movie_li.select('.ipc-html-content')

    print(f"[{title}]. \nReleased - {meta[0].text}, Length - {meta[1].text} | PG rating: {meta[2].text}\nRating: {rating[0].text} | Votes:{votes[0].text}.\n")