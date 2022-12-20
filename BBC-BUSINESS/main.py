from bs4 import BeautifulSoup
from csv import writer
import requests
import pprint
import time

# =================================Config=============================================
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


# ==========================================BUSINESS======================================

def export_business():
    endpoint = "https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-%7Blx-commentary-data-paged%2Fabout%2F19a1d11b-1755-4f97-8747-0c9534336a47%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F0%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2Fabout%2F19a1d11b-1755-4f97-8747-0c9534336a47%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2Fabout%2F19a1d11b-1755-4f97-8747-0c9534336a47%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F50%2Fversion%2F1.5.6%7D?timeout=5"
    response = requests.get(url=endpoint, headers=headers)
    data = response.json()

    articles = data["payload"][0]["body"]["results"]

    def get_author(element):
        try:
            return element['contributor']['name']
        except:
            return "NOT FOUND"

    articles_links = ["https://www.bbc.com" + article['url'] for article in articles]
    articles_images = [article['image']['href'] for article in articles]
    titles = [article['title'].replace("'", '') for article in articles]
    authors = [get_author(article) for article in articles]
    dates = [article['dateAdded'].split('T')[0] for article in articles]
    descriptions = [article['summary'].replace("'", '') for article in articles]

    for i in range(len(articles_links)):
        url = articles_links[i]
        article_response = requests.get(url=url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        text = soup.find_all('p', {'class': 'ssrcss-1q0x1qg-Paragraph'})

        text = text[:-1]

        content = [item.text + "\n" for item in text]
        content = "".join(content)
        with open('Business.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], articles_images[i], authors[i], dates[i],
                           descriptions[i], content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_business():
    endpoint = "https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-%7Blx-commentary-data-paged%2Fabout%2F19a1d11b-1755-4f97-8747-0c9534336a47%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F0%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2Fabout%2F19a1d11b-1755-4f97-8747-0c9534336a47%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2Fabout%2F19a1d11b-1755-4f97-8747-0c9534336a47%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F50%2Fversion%2F1.5.6%7D?timeout=5"
    response = requests.get(url=endpoint, headers=headers)
    data = response.json()

    article = data["payload"][0]["body"]["results"][0]

    def get_author(element):
        try:
            return element['contributor']['name']
        except:
            return "NOT FOUND"

    article_link = "https://www.bbc.com" + article['url']
    article_image = article['image']['href']
    title = article['title']
    author = get_author(article)
    date = article['dateAdded'].split('T')[0]
    description = article['summary']

    url = article_link
    article_response = requests.get(url=url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    text = soup.find_all('p', {'class': 'ssrcss-1q0x1qg-Paragraph'})

    text = text[:-1]

    content = [item.text + "\n" for item in text]
    content = "".join(content)

    article = {
        "article-link": article_link,
        "article-title": title,
        "article-img": article_image,
        "article-author": author,
        "date": date,
        "article-description": description,
        "article-content": content,
    }
    pprint.pprint(article)


# ==========================================New Economy======================================

def export_new_economy():
    endpoint = "https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-%7Blx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48039736%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F0%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48039736%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48039736%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F50%2Fversion%2F1.5.6%7D?timeout=5"
    response = requests.get(url=endpoint, headers=headers)
    data = response.json()

    articles = data["payload"][0]["body"]["results"]

    def get_author(element):
        try:
            return element['contributor']['name']
        except:
            return "NOT FOUND"

    articles_links = ["https://www.bbc.com" + article['url'] for article in articles]
    articles_images = [article['image']['href'] for article in articles]
    titles = [article['title'] for article in articles]
    authors = [get_author(article) for article in articles]
    dates = [article['dateAdded'].split('T')[0] for article in articles]
    descriptions = [article['summary'] for article in articles]

    for i in range(len(articles_links)):
        url = articles_links[i]
        article_response = requests.get(url=url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        text = soup.find_all('p', {'class': 'ssrcss-1q0x1qg-Paragraph'})

        text = text[:-1]

        content = [item.text + "\n" for item in text]
        content = "".join(content)
        with open('New_Economy.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], articles_images[i], authors[i], dates[i],
                           descriptions[i], content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_new_economy():
    endpoint = "https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-%7Blx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48039736%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F0%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48039736%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48039736%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F50%2Fversion%2F1.5.6%7D?timeout=5"
    response = requests.get(url=endpoint, headers=headers)
    data = response.json()

    article = data["payload"][0]["body"]["results"][0]

    def get_author(element):
        try:
            return element['contributor']['name']
        except:
            return "NOT FOUND"

    article_link = "https://www.bbc.com" + article['url']
    article_image = article['image']['href']
    title = article['title']
    author = get_author(article)
    date = article['dateAdded'].split('T')[0]
    description = article['summary']

    url = article_link
    article_response = requests.get(url=url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    text = soup.find_all('p', {'class': 'ssrcss-1q0x1qg-Paragraph'})

    text = text[:-1]

    content = [item.text + "\n" for item in text]
    content = "".join(content)

    article = {
        "article-link": article_link,
        "article-title": title,
        "article-img": article_image,
        "article-author": author,
        "date": date,
        "article-description": description,
        "article-content": content,
    }
    pprint.pprint(article)


# ==========================================New Tech Economy======================================

def export_new_tech_economy():
    endpoint = "https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-%7Blx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48296727%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F0%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48296727%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48296727%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F50%2Fversion%2F1.5.6%7D?timeout=5"
    response = requests.get(url=endpoint, headers=headers)
    data = response.json()

    articles = data["payload"][0]["body"]["results"]

    def get_author(element):
        try:
            return element['contributor']['name']
        except:
            return "NOT FOUND"

    articles_links = ["https://www.bbc.com" + article['url'] for article in articles]
    articles_images = [article['image']['href'] for article in articles]
    titles = [article['title'] for article in articles]
    authors = [get_author(article) for article in articles]
    dates = [article['dateAdded'].split('T')[0] for article in articles]
    descriptions = [article['summary'] for article in articles]

    for i in range(len(articles_links)):
        url = articles_links[i]
        article_response = requests.get(url=url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        text = soup.find_all('p', {'class': 'ssrcss-1q0x1qg-Paragraph'})

        text = text[:-1]

        content = [item.text + "\n" for item in text]
        content = "".join(content)
        with open('New_Tech_Economy.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], articles_images[i], authors[i], dates[i],
                           descriptions[i], content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_new_tech_economy():
    endpoint = "https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-%7Blx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48296727%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F0%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48296727%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48296727%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F50%2Fversion%2F1.5.6%7D?timeout=5"
    response = requests.get(url=endpoint, headers=headers)
    data = response.json()

    article = data["payload"][0]["body"]["results"][0]

    def get_author(element):
        try:
            return element['contributor']['name']
        except:
            return "NOT FOUND"

    article_link = "https://www.bbc.com" + article['url']
    article_image = article['image']['href']
    title = article['title']
    author = get_author(article)
    date = article['dateAdded'].split('T')[0]
    description = article['summary']

    url = article_link
    article_response = requests.get(url=url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    text = soup.find_all('p', {'class': 'ssrcss-1q0x1qg-Paragraph'})

    text = text[:-1]

    content = [item.text + "\n" for item in text]
    content = "".join(content)

    article = {
        "article-link": article_link,
        "article-title": title,
        "article-img": article_image,
        "article-author": author,
        "date": date,
        "article-description": description,
        "article-content": content,
    }
    pprint.pprint(article)


# ==========================================Companies======================================

def export_companies():
    endpoint = "https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-%7Blx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-47739214%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F0%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-47739214%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-47739214%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F50%2Fversion%2F1.5.6%7D?timeout=5"
    response = requests.get(url=endpoint, headers=headers)
    data = response.json()

    articles = data["payload"][0]["body"]["results"]

    def get_author(element):
        try:
            return element['contributor']['name']
        except:
            return "NOT FOUND"

    articles_links = ["https://www.bbc.com" + article['url'] for article in articles]
    articles_images = [article['image']['href'] for article in articles]
    titles = [article['title'] for article in articles]
    authors = [get_author(article) for article in articles]
    dates = [article['dateAdded'].split('T')[0] for article in articles]
    descriptions = [article['summary'] for article in articles]

    for i in range(len(articles_links)):
        url = articles_links[i]
        article_response = requests.get(url=url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        text = soup.find_all('p', {'class': 'ssrcss-1q0x1qg-Paragraph'})

        text = text[:-1]

        content = [item.text + "\n" for item in text]
        content = "".join(content)
        with open('Companies.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], articles_images[i], authors[i], dates[i],
                           descriptions[i], content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_companies():
    endpoint = "https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-%7Blx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-47739214%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F0%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-47739214%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-47739214%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F50%2Fversion%2F1.5.6%7D?timeout=5"
    response = requests.get(url=endpoint, headers=headers)
    data = response.json()

    article = data["payload"][0]["body"]["results"][0]

    def get_author(element):
        try:
            return element['contributor']['name']
        except:
            return "NOT FOUND"

    article_link = "https://www.bbc.com" + article['url']
    article_image = article['image']['href']
    title = article['title']
    author = get_author(article)
    date = article['dateAdded'].split('T')[0]
    description = article['summary']

    url = article_link
    article_response = requests.get(url=url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    text = soup.find_all('p', {'class': 'ssrcss-1q0x1qg-Paragraph'})

    text = text[:-1]

    content = [item.text + "\n" for item in text]
    content = "".join(content)

    article = {
        "article-link": article_link,
        "article-title": title,
        "article-img": article_image,
        "article-author": author,
        "date": date,
        "article-description": description,
        "article-content": content,
    }
    pprint.pprint(article)


# ==========================================Technology of Business======================================

def export_technology_of_business():
    endpoint = "https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-%7Blx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48039734%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F0%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48039734%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48039734%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F20%2Fversion%2F1.5.6%7D?timeout=5"
    response = requests.get(url=endpoint, headers=headers)
    data = response.json()

    articles = data["payload"][0]["body"]["results"]

    def get_author(element):
        try:
            return element['contributor']['name']
        except:
            return "NOT FOUND"

    def get_url(element):
        try:
            return "https://www.bbc.com" + element['url']
        except:
            return "NOT FOUND"

    def get_image(element):
        try:
            return element['image']['href']
        except:
            return "NOT FOUND"

    def get_description(element):
        try:
            return element['summary']
        except:
            return "NOT FOUND"

    articles_links = [get_url(article) for article in articles]
    articles_images = [get_image(article) for article in articles]
    titles = [article['title'] for article in articles]
    authors = [get_author(article) for article in articles]
    dates = [article['dateAdded'].split('T')[0] for article in articles]
    descriptions = [get_description(article) for article in articles]

    for i in range(len(articles_links)):
        url = articles_links[i]
        if url == "NOT FOUND":
            continue
        article_response = requests.get(url=url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        text = soup.find_all('p', {'class': 'ssrcss-1q0x1qg-Paragraph'})

        text = text[:-1]

        content = [item.text + "\n" for item in text]
        content = "".join(content)
        with open('Technology_of_Business.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], articles_images[i], authors[i], dates[i],
                           descriptions[i], content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_technology_of_business():
    endpoint = "https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-%7Blx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48039734%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F0%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48039734%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-48039734%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F20%2Fversion%2F1.5.6%7D?timeout=5"
    response = requests.get(url=endpoint, headers=headers)
    data = response.json()

    article = data["payload"][0]["body"]["results"][0]

    def get_author(element):
        try:
            return element['contributor']['name']
        except:
            return "NOT FOUND"

    article_link = "https://www.bbc.com" + article['url']
    article_image = article['image']['href']
    title = article['title']
    author = get_author(article)
    date = article['dateAdded'].split('T')[0]
    description = article['summary']

    url = article_link
    article_response = requests.get(url=url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    text = soup.find_all('p', {'class': 'ssrcss-1q0x1qg-Paragraph'})

    text = text[:-1]

    content = [item.text + "\n" for item in text]
    content = "".join(content)

    article = {
        "article-link": article_link,
        "article-title": title,
        "article-img": article_image,
        "article-author": author,
        "date": date,
        "article-description": description,
        "article-content": content,
    }
    pprint.pprint(article)


# ==========================================Economy======================================

def export_economy():
    endpoint = "https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-%7Blx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-47739220%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F0%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-47739220%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-47739220%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F50%2Fversion%2F1.5.6%7D?timeout=5"
    response = requests.get(url=endpoint, headers=headers)
    data = response.json()

    articles = data["payload"][0]["body"]["results"]

    def get_author(element):
        try:
            return element['contributor']['name']
        except:
            return "NOT FOUND"

    def get_url(element):
        try:
            return "https://www.bbc.com" + element['url']
        except:
            return "NOT FOUND"

    def get_image(element):
        try:
            return element['image']['href']
        except:
            return "NOT FOUND"

    def get_description(element):
        try:
            return element['summary']
        except:
            return "NOT FOUND"

    articles_links = [get_url(article) for article in articles]
    articles_images = [get_image(article) for article in articles]
    titles = [article['title'] for article in articles]
    authors = [get_author(article) for article in articles]
    dates = [article['dateAdded'].split('T')[0] for article in articles]
    descriptions = [get_description(article) for article in articles]

    for i in range(len(articles_links)):
        url = articles_links[i]
        if url == "NOT FOUND":
            continue
        article_response = requests.get(url=url, headers=headers)
        article_data = article_response.text
        soup = BeautifulSoup(article_data, 'html.parser')

        text = soup.find_all('p', {'class': 'ssrcss-1q0x1qg-Paragraph'})

        text = text[:-1]

        content = [item.text + "\n" for item in text]
        content = "".join(content)
        with open('Economy.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], titles[i], articles_images[i], authors[i], dates[i],
                           descriptions[i], content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_economy():
    endpoint = "https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-%7Blx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-47739220%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F0%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-47739220%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6%2Clx-commentary-data-paged%2FassetUri%2Fnews%252Flive%252Fbusiness-47739220%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F50%2Fversion%2F1.5.6%7D?timeout=5"
    response = requests.get(url=endpoint, headers=headers)
    data = response.json()

    article = data["payload"][0]["body"]["results"][0]

    def get_author(element):
        try:
            return element['contributor']['name']
        except:
            return "NOT FOUND"

    article_link = "https://www.bbc.com" + article['url']
    article_image = article['image']['href']
    title = article['title']
    author = get_author(article)
    date = article['dateAdded'].split('T')[0]
    description = article['summary']

    url = article_link
    article_response = requests.get(url=url, headers=headers)
    article_data = article_response.text
    soup = BeautifulSoup(article_data, 'html.parser')

    text = soup.find_all('p', {'class': 'ssrcss-1q0x1qg-Paragraph'})

    text = text[:-1]

    content = [item.text + "\n" for item in text]
    content = "".join(content)

    article = {
        "article-link": article_link,
        "article-title": title,
        "article-img": article_image,
        "article-author": author,
        "date": date,
        "article-description": description,
        "article-content": content,
    }
    pprint.pprint(article)

# ============================================Run Functions====================================
