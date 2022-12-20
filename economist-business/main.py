from bs4 import BeautifulSoup
from csv import writer
import requests
import pprint
import time

# ==================================Config==============================================
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


# ====================================Business===========================================

def export_business():
    url = "https://www.economist.com/business"
    response = requests.get(url=url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'css-juaghv'})
    images = soup.find_all('div', {'class': 'css-18uj6b0'})
    descriptions = soup.find_all('p', {'class': 'css-1tj7b79'})
    types = soup.find_all('p', {'class': 'css-24thab e1ulddkx0'})

    articles_links = ["https://www.economist.com" + item.find('a').get('href') for item in articles]
    articles_images = [image.find('img').get('src') for image in images]
    titles = [item.find('a').text for item in articles]
    articles_types = [item.text for item in types]
    articles_descriptions = [item.text for item in descriptions]

    for i in range(len(articles_links)):
        url = articles_links[i]
        article_response = requests.get(url=url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        text = soup.find_all('p', {'class': 'article__body-text'})
        content = [paragraph.text + '\n' for paragraph in text]
        content = "".join(content)

        try:
            date = soup.find("time").get('datetime').split('T')[0]
        except:
            date = 'NOT FOUND'

        with open('Business.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], articles_images[i], date, articles_types[i],
                           articles_descriptions[i], content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_business():
    url = "https://www.economist.com/business"
    response = requests.get(url=url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles_links = "https://www.economist.com" + soup.find('h3', {'class': 'css-juaghv'}).find('a').get('href')
    articles_images = soup.find('div', {'class': 'css-18uj6b0'}).find('img').get('src')
    articles_descriptions = soup.find('p', {'class': 'css-1tj7b79'}).text
    articles_types = soup.find('p', {'class': 'css-24thab e1ulddkx0'}).text
    titles = soup.find('h3', {'class': 'css-juaghv'}).find('a').text

    article_url = articles_links
    article_response = requests.get(url=article_url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    text = soup.find_all('p', {'class': 'article__body-text'})
    content = [paragraph.text + '\n' for paragraph in text]
    content = "".join(content)

    try:
        date = soup.find("time").get('datetime').split('T')[0]
    except:
        date = 'NOT FOUND'

    article = {
        "post_category": articles_types,
        "news_url": articles_links,
        "title": titles,
        "date": date,
        "image_url": articles_images,
        "description": articles_descriptions,
        "original_text": content,
    }
    pprint.pprint(article)


# ======================================RUN FUNCTION==========================================


