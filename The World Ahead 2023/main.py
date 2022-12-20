from bs4 import BeautifulSoup
from csv import writer
import requests
import pprint
import time

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


# ===============================================The World Ahead 2023===================================================

def export_the_world_ahead_2023():
    url = "https://www.economist.com/the-world-ahead-2023"
    response = requests.get(url=url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    aricles = soup.find_all('h3')

    articles_links = ["https://www.economist.com" + article.find('a').get('href') for article in aricles]
    titles = [article.find('a').text for article in aricles]
    time.sleep(2)

    print(len(articles_links))
    print(len(titles))

    for i in range(len(articles_links)):
        article_url = articles_links[i]
        article_response = requests.get(url=article_url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        try:
            image = soup.find('img').get('src')
        except:
            image = 'NOT FOUND'

        try:
            date = soup.find('time').get('datetime').split('T')[0]
        except:
            date = 'NOT FOUND'
        try:
            description = soup.find('h2', {'class': 'css-13b9ga2'}).text
        except:
            description = 'NOT FOUND'

        text = soup.find_all('p', {'class': 'article__body-text'})

        content = [paragraph.text + '\n' for paragraph in text]
        content = "".join(content)

        type = "The World Ahead 2023"

        with open('The World Ahead 2023.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], image, date, type,
                           description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_the_world_ahead_2023():
    url = "https://www.economist.com/the-world-ahead-2023"
    response = requests.get(url=url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    article = soup.find('h3')

    articles_links = "https://www.economist.com" + article.find('a').get('href')
    titles = article.find('a').text
    time.sleep(1)

    article_url = articles_links
    article_response = requests.get(url=article_url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    try:
        image = soup.find('img').get('src')
    except:
        image = 'NOT FOUND'

    try:
        date = soup.find('time').get('datetime').split('T')[0]
    except:
        date = 'NOT FOUND'
    try:
        description = soup.find('h2', {'class': 'css-13b9ga2'}).text
    except:
        description = 'NOT FOUND'

    text = soup.find_all('p', {'class': 'article__body-text'})

    content = [paragraph.text + '\n' for paragraph in text]
    content = "".join(content)

    type = "The World Ahead 2023"

    article = {
        "post_category": type,
        "news_url": articles_links,
        "title": titles,
        "date": date,
        "image_url": image,
        "description": description,
        "original_text": content,
    }
    pprint.pprint(article)


# =========================================RUN FUNCTION===========================================


