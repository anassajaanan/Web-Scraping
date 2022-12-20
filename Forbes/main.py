from bs4 import BeautifulSoup
from csv import writer
import requests
import pprint
import time


# ========================================Crypto & Blockchain==========================================
def export_crypto_blockchain():
    for i in range(2):
        START = 11 * i
        endpoint = f"https://www.forbes.com/simple-data/chansec/stream/?start={START}&limit=20&sourceValue=channel_72section_1095&" \
                   "swimLane=&specialSlot=crypto-blockchain&streamSourceType=channelsection"

        headers = {
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
                          "Safari/537.36"
        }

        response = requests.get(url=endpoint, headers=headers)
        data = response.json()['blocks']['items']

        for i in range(len(data)):
            article = data[i]
            article_type = article['type']
            if article_type == 'video':
                author = 'NOT FOUND'
                article_url = article['url']
                title = article['title']
                date = article['timestamp']
                image_url = article['image']
                description = article['description']

                if len(description) == 0:
                    description = 'NOT FOUND'

                content = 'VIDEO'
                article_type = "Crypto & Blockchain"

                with open('Crypto & Blockchain.csv', 'a', newline='', encoding="UTF-8") as file:
                    writer_object = writer(file)
                    try:
                        new_row = [article_url, title, image_url, author, date, article_type, description,
                                   content]
                    except:
                        pass
                    writer_object.writerow(new_row)
                file.close()
                time.sleep(1)

            else:
                author = article['author']['name']
                article_url = article['url']
                title = article['title']
                date = article['timestamp']
                image_url = article['image']
                description = article['description']

                if len(description) == 0:
                    description = 'NOT FOUND'

                article_response = requests.get(url=article_url, headers=headers)
                article_data = article_response.text
                soup = BeautifulSoup(article_data, 'html.parser')

                try:
                    text = soup.find('div', {'class': 'article-body'}).find_all('p')
                    content = [paragraph.text + '\n' for paragraph in text]
                    content = ''.join(content)
                except:
                    content = 'NOT FOUND'
                article_type = "Crypto & Blockchain"

                with open('Crypto & Blockchain.csv', 'a', newline='', encoding="UTF-8") as file:
                    writer_object = writer(file)
                    try:
                        new_row = [article_url, title, image_url, author, date, article_type, description,
                                   content]
                    except:
                        pass
                    writer_object.writerow(new_row)
                file.close()
                time.sleep(1)


def get_crypto_blockchain():
    endpoint = "https://www.forbes.com/simple-data/chansec/stream/?start=1&limit=20&sourceValue=channel_72section_1095&" \
               "swimLane=&specialSlot=crypto-blockchain&streamSourceType=channelsection"

    headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
                      "Safari/537.36"
    }

    response = requests.get(url=endpoint, headers=headers)
    data = response.json()['blocks']['items']

    article = data[0]
    article_type = article['type']
    if article_type == 'video':
        author = 'NOT FOUND'
        article_url = article['url']
        title = article['title']
        date = article['timestamp']
        image_url = article['image']
        description = article['description']
        if len(description) == 0:
            description = 'NOT FOUND'
        content = 'VIDEO'
        article_type = "Crypto & Blockchain"

        article = {
            "post_category": "Crypto & Blockchain",
            "news_url": article_url,
            "title": title,
            "date": date,
            "author": author,
            "image_url": image_url,
            "description": description,
            "original_text": content,
        }
        pprint.pprint(article)
        time.sleep(1)

    else:
        author = article['author']['name']
        article_url = article['url']
        title = article['title']
        date = article['timestamp']
        image_url = article['image']
        description = article['description']
        if len(description) == 0:
            description = 'NOT FOUND'

        article_response = requests.get(url=article_url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        try:
            text = soup.find('div', {'class': 'article-body'}).find_all('p')
            content = [paragraph.text + '\n' for paragraph in text]
            content = ''.join(content)
        except:
            content = 'NOT FOUND'
        article_type = "Crypto & Blockchain"

        article = {
            "post_category": "Crypto & Blockchain",
            "news_url": article_url,
            "title": title,
            "date": date,
            "author": author,
            "image_url": image_url,
            "description": description,
            "original_text": content,
        }
        pprint.pprint(article)
        time.sleep(1)

# ========================================RUN FUNCTIONS==========================================
