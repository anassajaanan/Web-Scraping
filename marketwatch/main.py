from bs4 import BeautifulSoup
from csv import writer
import requests
import pprint
import time

# =========================================Config==================================================
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


# ============================================Stocks===================================================
def export_stocks():
    Stocks_url = "https://www.marketwatch.com/investing/stocks?mod=investing"
    response = requests.get(url=Stocks_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 6 or images.index(image) > 15 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    time.sleep(1)

    for i in range(len(articles_links)):
        article_url = articles_links[i]
        article_response = requests.get(url=article_url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        article_type = 'Stocks'
        try:
            date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
        except:
            date = 'NOT FOUND'

        try:
            author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
            author = [item for item in author if item != '']
            author = [item + " " for item in author]
            author = "".join(author)
        except:
            author = 'NOT FOUND'

        try:
            description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
        except:
            description = 'NOT FOUND'
        if len(description) == 0:
            description = 'NOT FOUND'

        try:
            text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
            content = [item.text + "\n" for item in text]
            content = "".join(content)
        except:
            content = 'NOT FOUND'

        with open('Stocks.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [article_url, titles[i], articles_images[i], author, date, article_type, description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_stocks():
    Stocks_url = "https://www.marketwatch.com/investing/stocks?mod=investing"
    response = requests.get(url=Stocks_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 6 or images.index(image) > 15 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    time.sleep(1)

    article_url = articles_links[0]
    article_response = requests.get(url=article_url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    article_type = 'Stocks'
    try:
        date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
    except:
        date = 'NOT FOUND'

    try:
        author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
        author = [item for item in author if item != '']
        author = [item + " " for item in author]
        author = "".join(author)
    except:
        author = 'NOT FOUND'

    try:
        description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
    except:
        description = 'NOT FOUND'
    if len(description) == 0:
        description = 'NOT FOUND'

    try:
        text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
        content = [item.text + "\n" for item in text]
        content = "".join(content)
    except:
        content = 'NOT FOUND'

    article = {
        "post_category": article_type,
        "news_url": article_url,
        "title": titles[0],
        "author": author,
        "date": date,
        "image_url": articles_images[0],
        "description": description,
        "original_text": content,
    }

    pprint.pprint(article)


# ============================================Funds===================================================
def export_funds():
    Funds_url = "https://www.marketwatch.com/investing/mutual-funds?mod=stocks"
    response = requests.get(url=Funds_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 5 or images.index(image) > 14 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    titles = titles[1:]
    articles_links = articles_links[1:]

    time.sleep(1)

    for i in range(len(articles_links)):
        article_url = articles_links[i]
        article_response = requests.get(url=article_url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        article_type = 'Funds'
        try:
            date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
        except:
            date = 'NOT FOUND'

        try:
            author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
            author = [item for item in author if item != '']
            author = [item + " " for item in author]
            author = "".join(author)
        except:
            author = 'NOT FOUND'

        try:
            description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
        except:
            description = 'NOT FOUND'
        if len(description) == 0:
            description = 'NOT FOUND'

        try:
            text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
            content = [item.text + "\n" for item in text]
            content = "".join(content)
        except:
            content = 'NOT FOUND'

        with open('Funds.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [article_url, titles[i], articles_images[i], author, date, article_type, description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_funds():
    Funds_url = "https://www.marketwatch.com/investing/mutual-funds?mod=stocks"
    response = requests.get(url=Funds_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 5 or images.index(image) > 14 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    time.sleep(1)

    article_url = articles_links[0]
    article_response = requests.get(url=article_url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    article_type = 'Funds'
    try:
        date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
    except:
        date = 'NOT FOUND'

    try:
        author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
        author = [item for item in author if item != '']
        author = [item + " " for item in author]
        author = "".join(author)
    except:
        author = 'NOT FOUND'

    try:
        description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
    except:
        description = 'NOT FOUND'
    if len(description) == 0:
        description = 'NOT FOUND'

    try:
        text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
        content = [item.text + "\n" for item in text]
        content = "".join(content)
    except:
        content = 'NOT FOUND'

    article = {
        "post_category": article_type,
        "news_url": article_url,
        "title": titles[0],
        "author": author,
        "date": date,
        "image_url": articles_images[0],
        "description": description,
        "original_text": content,
    }

    pprint.pprint(article)


# ============================================Exchange-Traded Funds===================================================
def export_etfs():
    ETFs_url = "https://www.marketwatch.com/investing/etf?mod=mutual-funds"
    response = requests.get(url=ETFs_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 5 or images.index(image) > 14 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    titles = titles[1:]
    articles_links = articles_links[1:]

    time.sleep(1)

    for i in range(len(articles_links)):
        article_url = articles_links[i]
        article_response = requests.get(url=article_url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        article_type = 'Exchange-Traded Funds'
        try:
            date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
        except:
            date = 'NOT FOUND'

        try:
            author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
            author = [item for item in author if item != '']
            author = [item + " " for item in author]
            author = "".join(author)
        except:
            author = 'NOT FOUND'

        try:
            description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
        except:
            description = 'NOT FOUND'
        if len(description) == 0:
            description = 'NOT FOUND'

        try:
            text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
            content = [item.text + "\n" for item in text]
            content = "".join(content)
        except:
            content = 'NOT FOUND'

        with open('ETFs.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [article_url, titles[i], articles_images[i], author, date, article_type, description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_etfs():
    ETFs_url = "https://www.marketwatch.com/investing/etf?mod=mutual-funds"
    response = requests.get(url=ETFs_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 5 or images.index(image) > 14 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    time.sleep(1)

    article_url = articles_links[0]
    article_response = requests.get(url=article_url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    article_type = 'Exchange-Traded Funds'
    try:
        date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
    except:
        date = 'NOT FOUND'

    try:
        author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
        author = [item for item in author if item != '']
        author = [item + " " for item in author]
        author = "".join(author)
    except:
        author = 'NOT FOUND'

    try:
        description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
    except:
        description = 'NOT FOUND'
    if len(description) == 0:
        description = 'NOT FOUND'

    try:
        text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
        content = [item.text + "\n" for item in text]
        content = "".join(content)
    except:
        content = 'NOT FOUND'

    article = {
        "post_category": article_type,
        "news_url": article_url,
        "title": titles[0],
        "author": author,
        "date": date,
        "image_url": articles_images[0],
        "description": description,
        "original_text": content,
    }

    pprint.pprint(article)


# ============================================Bonds===================================================
def export_bonds():
    Bonds_url = "https://www.marketwatch.com/investing/bonds?mod=exchange-traded-funds"
    response = requests.get(url=Bonds_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 6 or images.index(image) > 15 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    time.sleep(1)

    for i in range(len(articles_links)):
        article_url = articles_links[i]
        article_response = requests.get(url=article_url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        article_type = 'Bonds'
        try:
            date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
        except:
            date = 'NOT FOUND'

        try:
            author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
            author = [item for item in author if item != '']
            author = [item + " " for item in author]
            author = "".join(author)
        except:
            author = 'NOT FOUND'

        try:
            description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
        except:
            description = 'NOT FOUND'
        if len(description) == 0:
            description = 'NOT FOUND'

        try:
            text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
            content = [item.text + "\n" for item in text]
            content = "".join(content)
        except:
            content = 'NOT FOUND'

        with open('Bonds.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [article_url, titles[i], articles_images[i], author, date, article_type, description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_bonds():
    Bonds_url = "https://www.marketwatch.com/investing/bonds?mod=exchange-traded-funds"
    response = requests.get(url=Bonds_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 6 or images.index(image) > 15 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    time.sleep(1)

    article_url = articles_links[0]
    article_response = requests.get(url=article_url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    article_type = 'Bonds'
    try:
        date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
    except:
        date = 'NOT FOUND'

    try:
        author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
        author = [item for item in author if item != '']
        author = [item + " " for item in author]
        author = "".join(author)
    except:
        author = 'NOT FOUND'

    try:
        description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
    except:
        description = 'NOT FOUND'
    if len(description) == 0:
        description = 'NOT FOUND'

    try:
        text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
        content = [item.text + "\n" for item in text]
        content = "".join(content)
    except:
        content = 'NOT FOUND'

    article = {
        "post_category": article_type,
        "news_url": article_url,
        "title": titles[0],
        "author": author,
        "date": date,
        "image_url": articles_images[0],
        "description": description,
        "original_text": content,
    }

    pprint.pprint(article)


# ============================================Futures===================================================
def export_futures():
    Futures_url = "https://www.marketwatch.com/investing/futures?mod=bonds"
    response = requests.get(url=Futures_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 5 or images.index(image) > 14 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    # titles = titles[1:]
    # articles_links = articles_links[1:]

    time.sleep(1)

    for i in range(len(articles_links)):
        article_url = articles_links[i]
        article_response = requests.get(url=article_url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        article_type = 'Futures'
        try:
            date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
        except:
            date = 'NOT FOUND'

        try:
            author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
            author = [item for item in author if item != '']
            author = [item + " " for item in author]
            author = "".join(author)
        except:
            author = 'NOT FOUND'

        try:
            description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
        except:
            description = 'NOT FOUND'
        if len(description) == 0:
            description = 'NOT FOUND'

        try:
            text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
            content = [item.text + "\n" for item in text]
            content = "".join(content)
        except:
            content = 'NOT FOUND'

        with open('Futures.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [article_url, titles[i], articles_images[i], author, date, article_type, description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_futures():
    Futures_url = "https://www.marketwatch.com/investing/futures?mod=bonds"
    response = requests.get(url=Futures_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 5 or images.index(image) > 14 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    time.sleep(1)

    article_url = articles_links[0]
    article_response = requests.get(url=article_url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    article_type = 'Futures'
    try:
        date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
    except:
        date = 'NOT FOUND'

    try:
        author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
        author = [item for item in author if item != '']
        author = [item + " " for item in author]
        author = "".join(author)
    except:
        author = 'NOT FOUND'

    try:
        description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
    except:
        description = 'NOT FOUND'
    if len(description) == 0:
        description = 'NOT FOUND'

    try:
        text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
        content = [item.text + "\n" for item in text]
        content = "".join(content)
    except:
        content = 'NOT FOUND'

    article = {
        "post_category": article_type,
        "news_url": article_url,
        "title": titles[0],
        "author": author,
        "date": date,
        "image_url": articles_images[0],
        "description": description,
        "original_text": content,
    }

    pprint.pprint(article)


# ============================================Cryptocurrencies===================================================
def export_crypto():
    crypto_url = "https://www.marketwatch.com/investing/cryptocurrency?mod=futures"
    response = requests.get(url=crypto_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 3 or images.index(image) > 12 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    # titles = titles[1:]
    # articles_links = articles_links[1:]

    time.sleep(1)

    for i in range(len(articles_links)):
        article_url = articles_links[i]
        article_response = requests.get(url=article_url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        article_type = 'Cryptocurrencies'
        try:
            date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
        except:
            date = 'NOT FOUND'

        try:
            author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
            author = [item for item in author if item != '']
            author = [item + " " for item in author]
            author = "".join(author)
        except:
            author = 'NOT FOUND'

        try:
            description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
        except:
            description = 'NOT FOUND'
        if len(description) == 0:
            description = 'NOT FOUND'

        try:
            text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
            content = [item.text + "\n" for item in text]
            content = "".join(content)
        except:
            content = 'NOT FOUND'

        with open('Cryptocurrencies.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [article_url, titles[i], articles_images[i], author, date, article_type, description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_crypto():
    crypto_url = "https://www.marketwatch.com/investing/cryptocurrency?mod=futures"
    response = requests.get(url=crypto_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 5 or images.index(image) > 14 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    time.sleep(1)

    article_url = articles_links[0]
    article_response = requests.get(url=article_url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    article_type = 'Cryptocurrencies'
    try:
        date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
    except:
        date = 'NOT FOUND'

    try:
        author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
        author = [item for item in author if item != '']
        author = [item + " " for item in author]
        author = "".join(author)
    except:
        author = 'NOT FOUND'

    try:
        description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
    except:
        description = 'NOT FOUND'
    if len(description) == 0:
        description = 'NOT FOUND'

    try:
        text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
        content = [item.text + "\n" for item in text]
        content = "".join(content)
    except:
        content = 'NOT FOUND'

    article = {
        "post_category": article_type,
        "news_url": article_url,
        "title": titles[0],
        "author": author,
        "date": date,
        "image_url": articles_images[0],
        "description": description,
        "original_text": content,
    }

    pprint.pprint(article)


# ============================================Fx Currencies===================================================
def export_currencies():
    Currencies_url = "https://www.marketwatch.com/investing/currencies?mod=currencies"
    response = requests.get(url=Currencies_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 5 or images.index(image) > 14 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    # titles = titles[1:]
    # articles_links = articles_links[1:]

    time.sleep(1)

    for i in range(len(articles_links)):
        article_url = articles_links[i]
        article_response = requests.get(url=article_url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        article_type = 'Currencies'
        try:
            date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
        except:
            date = 'NOT FOUND'

        try:
            author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
            author = [item for item in author if item != '']
            author = [item + " " for item in author]
            author = "".join(author)
        except:
            author = 'NOT FOUND'

        try:
            description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
        except:
            description = 'NOT FOUND'
        if len(description) == 0:
            description = 'NOT FOUND'

        try:
            text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
            content = [item.text + "\n" for item in text]
            content = "".join(content)
        except:
            content = 'NOT FOUND'

        with open('Currencies.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [article_url, titles[i], articles_images[i], author, date, article_type, description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_currencies():
    Currencies_url = "https://www.marketwatch.com/investing/currencies?mod=currencies"
    response = requests.get(url=Currencies_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 5 or images.index(image) > 14 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    time.sleep(1)

    article_url = articles_links[0]
    article_response = requests.get(url=article_url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    article_type = 'Currencies'
    try:
        date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
    except:
        date = 'NOT FOUND'

    try:
        author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
        author = [item for item in author if item != '']
        author = [item + " " for item in author]
        author = "".join(author)
    except:
        author = 'NOT FOUND'

    try:
        description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
    except:
        description = 'NOT FOUND'
    if len(description) == 0:
        description = 'NOT FOUND'

    try:
        text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
        content = [item.text + "\n" for item in text]
        content = "".join(content)
    except:
        content = 'NOT FOUND'

    article = {
        "post_category": article_type,
        "news_url": article_url,
        "title": titles[0],
        "author": author,
        "date": date,
        "image_url": articles_images[0],
        "description": description,
        "original_text": content,
    }

    pprint.pprint(article)


# ============================================Options===================================================
def export_options():
    Options_url = "https://www.marketwatch.com/investing/options?mod=currencies"
    response = requests.get(url=Options_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 6 or images.index(image) > 11 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    # titles = titles[1:]
    # articles_links = articles_links[1:]

    time.sleep(1)

    for i in range(len(articles_links)):
        article_url = articles_links[i]
        article_response = requests.get(url=article_url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        article_type = 'Options'
        try:
            date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
        except:
            date = 'NOT FOUND'

        try:
            author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
            author = [item for item in author if item != '']
            author = [item + " " for item in author]
            author = "".join(author)
        except:
            author = 'NOT FOUND'

        try:
            description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
        except:
            description = 'NOT FOUND'
        if len(description) == 0:
            description = 'NOT FOUND'

        try:
            text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
            content = [item.text + "\n" for item in text]
            content = "".join(content)
        except:
            content = 'NOT FOUND'

        with open('Options.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [article_url, titles[i], articles_images[i], author, date, article_type, description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_options():
    Options_url = "https://www.marketwatch.com/investing/options?mod=currencies"
    response = requests.get(url=Options_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 5 or images.index(image) > 14 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    time.sleep(1)

    article_url = articles_links[0]
    article_response = requests.get(url=article_url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    article_type = 'Options'
    try:
        date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
    except:
        date = 'NOT FOUND'

    try:
        author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
        author = [item for item in author if item != '']
        author = [item + " " for item in author]
        author = "".join(author)
    except:
        author = 'NOT FOUND'

    try:
        description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
    except:
        description = 'NOT FOUND'
    if len(description) == 0:
        description = 'NOT FOUND'

    try:
        text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
        content = [item.text + "\n" for item in text]
        content = "".join(content)
    except:
        content = 'NOT FOUND'

    article = {
        "post_category": article_type,
        "news_url": article_url,
        "title": titles[0],
        "author": author,
        "date": date,
        "image_url": articles_images[0],
        "description": description,
        "original_text": content,
    }

    pprint.pprint(article)


# ==========================================Initial Public Offerings=================================================
def export_initial_public_offerings():
    initial_public_offerings_url = "https://www.marketwatch.com/investing/ipo?mod=options"
    response = requests.get(url=initial_public_offerings_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 11 or images.index(image) > 21 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    # titles = titles[1:]
    # articles_links = articles_links[1:]

    time.sleep(1)

    for i in range(len(articles_links)):
        article_url = articles_links[i]
        article_response = requests.get(url=article_url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        article_type = 'Initial Public Offerings'
        try:
            date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
        except:
            date = 'NOT FOUND'

        try:
            author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
            author = [item for item in author if item != '']
            author = [item + " " for item in author]
            author = "".join(author)
        except:
            author = 'NOT FOUND'

        try:
            description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
        except:
            description = 'NOT FOUND'
        if len(description) == 0:
            description = 'NOT FOUND'

        try:
            text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
            content = [item.text + "\n" for item in text]
            content = "".join(content)
        except:
            content = 'NOT FOUND'

        with open('Initial Public Offerings.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [article_url, titles[i], articles_images[i], author, date, article_type, description, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_initial_public_offerings():
    initial_public_offerings_url = "https://www.marketwatch.com/investing/ipo?mod=options"
    response = requests.get(url=initial_public_offerings_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    articles = soup.find_all('h3', {'class': 'article__headline'})
    images = soup.find_all('a', {'class': 'figure__image'})

    def get_image(element):
        try:
            img = element.find('img').get('data-srcset')
            return img
        except:
            return 'NOT FOUND'

    def get_title(element):
        try:
            title = element.find('a', {'class': 'link'}).text.replace('                            ', '').replace('\n',
                                                                                                                  ''). \
                replace('                        ', '')
            return title
        except:
            return None

    def get_link(element):
        try:
            link = element.find('a', {'class': 'link'}).get('href')
            return link
        except:
            return None

    articles_images = [get_image(image) for image in images if
                       images.index(image) < 5 or images.index(image) > 14 and get_image(image) != None]
    articles_images = [item.split(',')[-1].replace(' 1240w', '') for item in articles_images]
    articles_links = [get_link(article) for article in articles if
                      get_link(article) != None and get_link(article) != '#']
    titles = [get_title(article) for article in articles if get_title(article) != None and get_title(article) != '']

    time.sleep(1)

    article_url = articles_links[0]
    article_response = requests.get(url=article_url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    article_type = 'Initial Public Offerings'
    try:
        date = soup.find('time').text.replace('\n', '').replace('    ', '').split(':')[1]
    except:
        date = 'NOT FOUND'

    try:
        author = soup.find('div', {'class': 'byline article__byline'}).text.split('\n')
        author = [item for item in author if item != '']
        author = [item + " " for item in author]
        author = "".join(author)
    except:
        author = 'NOT FOUND'

    try:
        description = soup.find('h2', {'class': 'article__subhead'}).text.replace('  ', '').replace('\n', '', 1)
    except:
        description = 'NOT FOUND'
    if len(description) == 0:
        description = 'NOT FOUND'

    try:
        text = soup.find('div', {'id': 'js-article__body'}).find_all('p')
        content = [item.text + "\n" for item in text]
        content = "".join(content)
    except:
        content = 'NOT FOUND'

    article = {
        "post_category": article_type,
        "news_url": article_url,
        "title": titles[0],
        "author": author,
        "date": date,
        "image_url": articles_images[0],
        "description": description,
        "original_text": content,
    }

    pprint.pprint(article)

# ===========================================RUN FUNCTION====================================================
