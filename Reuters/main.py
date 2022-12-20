from bs4 import BeautifulSoup
import requests
from csv import writer
import pprint
import time


# ==========Aerospace and Defense=============
def export_aerospace_and_defense():
    for j in range(2):
        id = f"{9 * j}"
        URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22id%22%3A%22%2Fbusiness%2Faerospace-defense%2F%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Faerospace-defense%2F%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22*%22%2C%22sophi_widget%22%3A%22topic%22%2C%22uri%22%3A%22%2Fbusiness%2Faerospace-defense%2F%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
        headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

        response = requests.get(url=URL, headers=headers)
        data = response.json()

        for i in range(len(data["result"]["articles"])):
            article_url = "https://www.reuters.com" + data["result"]["articles"][i]["canonical_url"]
            title = data["result"]["articles"][i]["title"].replace("'", "").replace(",", " ")
            description = data["result"]["articles"][i]["description"].replace("'", "").replace(",", " ")
            date = data["result"]["articles"][i]["published_time"].split("T")[0]
            try:
                image_url = data["result"]["articles"][i]["thumbnail"]["url"]
            except:
                image_url = "Not Found"

            article_response = requests.get(article_url)
            article_data = article_response.text

            soup = BeautifulSoup(article_data, "html.parser")
            content = soup.find_all("p", {
                "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
            content = [item.text + "\n" for item in content]
            content = "".join(content).replace("'", "").replace(",", " ")
            with open('Aerospace and Defense.csv', 'a', newline='', encoding="UTF-8") as file:
                writer_object = writer(file)
                try:
                    new_row = [article_url, title, date, image_url, description, content]
                except:
                    pass
                writer_object.writerow(new_row)
            file.close()


def get_aerospace_and_defense():
    id = "0"
    URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22id%22%3A%22%2Fbusiness%2Faerospace-defense%2F%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Faerospace-defense%2F%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22*%22%2C%22sophi_widget%22%3A%22topic%22%2C%22uri%22%3A%22%2Fbusiness%2Faerospace-defense%2F%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
    headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

    response = requests.get(url=URL, headers=headers)
    data = response.json()

    article_url = "https://www.reuters.com" + data["result"]["articles"][0]["canonical_url"]
    title = data["result"]["articles"][0]["title"]
    description = data["result"]["articles"][0]["description"]
    date = data["result"]["articles"][0]["published_time"].split("T")[0]
    try:
        image_url = data["result"]["articles"][0]["thumbnail"]["url"]
    except:
        image_url = "Not Found"

    article_response = requests.get(article_url)
    article_data = article_response.text

    soup = BeautifulSoup(article_data, "html.parser")
    content = soup.find_all("p", {
        "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
    content = [item.text + "\n" for item in content]
    content = "".join(content)
    article = {
        "type": "Aerospace and Defense",
        "article_url": article_url,
        "title": title,
        "date": date,
        "image_url": image_url,
        "description": description,
        "content": content
    }
    pprint.pprint(article)


# ===========Autos & Transporations============

def export_autos_and_transporations():
    for j in range(2):
        id = f"{9 * j}"
        URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22id%22%3A%22%2Fbusiness%2Fautos-transportation%2F%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Fautos-transportation%2F%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22*%22%2C%22sophi_widget%22%3A%22topic%22%2C%22uri%22%3A%22%2Fbusiness%2Fautos-transportation%2F%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
        headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

        response = requests.get(url=URL, headers=headers)
        data = response.json()

        for i in range(len(data["result"]["articles"])):
            article_url = "https://www.reuters.com" + data["result"]["articles"][i]["canonical_url"]
            title = data["result"]["articles"][i]["title"].replace("'", "").replace(",", " ")
            description = data["result"]["articles"][i]["description"].replace("'", "").replace(",", " ")
            date = data["result"]["articles"][i]["published_time"].split("T")[0]
            try:
                image_url = data["result"]["articles"][i]["thumbnail"]["url"]
            except:
                image_url = "Not Found"

            article_response = requests.get(article_url)
            article_data = article_response.text

            soup = BeautifulSoup(article_data, "html.parser")
            content = soup.find_all("p", {
                "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
            content = [item.text + "\n" for item in content]
            content = "".join(content).replace("'", "").replace(",", " ")
            with open('Autos & Transportation.csv', 'a', newline='', encoding="UTF-8") as file:
                writer_object = writer(file)
                try:
                    new_row = [article_url, title, date, image_url, description, content]
                except:
                    pass
                writer_object.writerow(new_row)
            file.close()


def get_autos_and_transporations():
    id = "0"
    URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22id%22%3A%22%2Fbusiness%2Fautos-transportation%2F%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Fautos-transportation%2F%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22*%22%2C%22sophi_widget%22%3A%22topic%22%2C%22uri%22%3A%22%2Fbusiness%2Fautos-transportation%2F%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
    headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

    response = requests.get(url=URL, headers=headers)
    data = response.json()

    article_url = "https://www.reuters.com" + data["result"]["articles"][0]["canonical_url"]
    title = data["result"]["articles"][0]["title"]
    description = data["result"]["articles"][0]["description"]
    date = data["result"]["articles"][0]["published_time"].split("T")[0]
    try:
        image_url = data["result"]["articles"][0]["thumbnail"]["url"]
    except:
        image_url = "Not Found"

    article_response = requests.get(article_url)
    article_data = article_response.text

    soup = BeautifulSoup(article_data, "html.parser")
    content = soup.find_all("p", {
        "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
    content = [item.text + "\n" for item in content]
    content = "".join(content)
    article = {
        "type": "Aerospace and Defense",
        "article_url": article_url,
        "title": title,
        "date": date,
        "image_url": image_url,
        "description": description,
        "content": content
    }
    pprint.pprint(article)


# ==========Environment===================

def export_environment():
    for j in range(2):
        id = f"{9 * j}"
        URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Fenvironment%2F%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22*%22%2C%22sophi_widget%22%3A%22topic%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
        headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

        response = requests.get(url=URL, headers=headers)
        data = response.json()

        for i in range(len(data["result"]["articles"])):
            article_url = "https://www.reuters.com" + data["result"]["articles"][i]["canonical_url"]
            title = data["result"]["articles"][i]["title"].replace("'", "").replace(",", " ")
            description = data["result"]["articles"][i]["description"].replace("'", "").replace(",", " ")
            date = data["result"]["articles"][i]["published_time"].split("T")[0]
            try:
                image_url = data["result"]["articles"][i]["thumbnail"]["url"]
            except:
                image_url = "Not Found"

            article_response = requests.get(article_url)
            article_data = article_response.text

            soup = BeautifulSoup(article_data, "html.parser")
            content = soup.find_all("p", {
                "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
            content = [item.text + "\n" for item in content]
            content = "".join(content).replace("'", "").replace(",", " ")
            with open('environment.csv', 'a', newline='', encoding="UTF-8") as file:
                writer_object = writer(file)
                try:
                    new_row = [article_url, title, date, image_url, description, content]
                except:
                    pass
                writer_object.writerow(new_row)
            file.close()


def get_environment():
    id = "0"
    URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Fenvironment%2F%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22*%22%2C%22sophi_widget%22%3A%22topic%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
    headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

    response = requests.get(url=URL, headers=headers)
    data = response.json()

    article_url = "https://www.reuters.com" + data["result"]["articles"][0]["canonical_url"]
    title = data["result"]["articles"][0]["title"]
    description = data["result"]["articles"][0]["description"]
    date = data["result"]["articles"][0]["published_time"].split("T")[0]
    try:
        image_url = data["result"]["articles"][0]["thumbnail"]["url"]
    except:
        image_url = "Not Found"

    article_response = requests.get(article_url)
    article_data = article_response.text

    soup = BeautifulSoup(article_data, "html.parser")
    content = soup.find_all("p", {
        "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
    content = [item.text + "\n" for item in content]
    content = "".join(content)
    article = {
        "type": "Aerospace and Defense",
        "article_url": article_url,
        "title": title,
        "date": date,
        "image_url": image_url,
        "description": description,
        "content": content
    }
    pprint.pprint(article)


# ==================Finance==================

def export_finance():
    for j in range(2):
        id = f"{9 * j}"
        URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22id%22%3A%22%2Fbusiness%2Ffinance%2F%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Ffinance%2F%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22*%22%2C%22sophi_widget%22%3A%22topic%22%2C%22uri%22%3A%22%2Fbusiness%2Ffinance%2F%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
        headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

        response = requests.get(url=URL, headers=headers)
        data = response.json()

        for i in range(len(data["result"]["articles"])):
            article_url = "https://www.reuters.com" + data["result"]["articles"][i]["canonical_url"]
            title = data["result"]["articles"][i]["title"].replace("'", "").replace(",", " ")
            description = data["result"]["articles"][i]["description"].replace("'", "").replace(",", " ")
            date = data["result"]["articles"][i]["published_time"].split("T")[0]
            try:
                image_url = data["result"]["articles"][i]["thumbnail"]["url"]
            except:
                image_url = "Not Found"

            article_response = requests.get(article_url)
            article_data = article_response.text

            soup = BeautifulSoup(article_data, "html.parser")
            content = soup.find_all("p", {
                "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
            content = [item.text + "\n" for item in content]
            content = "".join(content).replace("'", "").replace(",", " ")
            with open('Finance.csv', 'a', newline='', encoding="UTF-8") as file:
                writer_object = writer(file)
                try:
                    new_row = [article_url, title, date, image_url, description, content]
                except:
                    pass
                writer_object.writerow(new_row)
            file.close()


def get_finance():
    id = "0"
    URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22id%22%3A%22%2Fbusiness%2Ffinance%2F%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Ffinance%2F%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22*%22%2C%22sophi_widget%22%3A%22topic%22%2C%22uri%22%3A%22%2Fbusiness%2Ffinance%2F%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
    headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

    response = requests.get(url=URL, headers=headers)
    data = response.json()

    article_url = "https://www.reuters.com" + data["result"]["articles"][0]["canonical_url"]
    title = data["result"]["articles"][0]["title"]
    description = data["result"]["articles"][0]["description"]
    date = data["result"]["articles"][0]["published_time"].split("T")[0]
    try:
        image_url = data["result"]["articles"][0]["thumbnail"]["url"]
    except:
        image_url = "Not Found"

    article_response = requests.get(article_url)
    article_data = article_response.text

    soup = BeautifulSoup(article_data, "html.parser")
    content = soup.find_all("p", {
        "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
    content = [item.text + "\n" for item in content]
    content = "".join(content)
    article = {
        "type": "Aerospace and Defense",
        "article_url": article_url,
        "title": title,
        "date": date,
        "image_url": image_url,
        "description": description,
        "content": content
    }
    pprint.pprint(article)


# =============HealthCare=======================

def export_healthcare():
    for j in range(2):
        id = f"{9 * j}"
        URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22id%22%3A%22%2Fbusiness%2Fhealthcare-pharmaceuticals%2F%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Fhealthcare-pharmaceuticals%2F%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22*%22%2C%22sophi_widget%22%3A%22topic%22%2C%22uri%22%3A%22%2Fbusiness%2Fhealthcare-pharmaceuticals%2F%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
        headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

        response = requests.get(url=URL, headers=headers)
        data = response.json()

        for i in range(len(data["result"]["articles"])):
            article_url = "https://www.reuters.com" + data["result"]["articles"][i]["canonical_url"]
            title = data["result"]["articles"][i]["title"].replace("'", "").replace(",", " ")
            description = data["result"]["articles"][i]["description"].replace("'", "").replace(",", " ")
            date = data["result"]["articles"][i]["published_time"].split("T")[0]
            try:
                image_url = data["result"]["articles"][i]["thumbnail"]["url"]
            except:
                image_url = "Not Found"

            article_response = requests.get(article_url)
            article_data = article_response.text

            soup = BeautifulSoup(article_data, "html.parser")
            content = soup.find_all("p", {
                "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
            content = [item.text + "\n" for item in content]
            content = "".join(content).replace("'", "").replace(",", " ")

            with open('HealthCare.csv', 'a', newline='', encoding="UTF-8") as file:
                writer_object = writer(file)
                try:
                    new_row = [article_url, title, date, image_url, description, content]
                except:
                    pass
                writer_object.writerow(new_row)
            file.close()


def get_healthcare():
    id = "0"
    URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22id%22%3A%22%2Fbusiness%2Fhealthcare-pharmaceuticals%2F%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Fhealthcare-pharmaceuticals%2F%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22*%22%2C%22sophi_widget%22%3A%22topic%22%2C%22uri%22%3A%22%2Fbusiness%2Fhealthcare-pharmaceuticals%2F%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
    headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

    response = requests.get(url=URL, headers=headers)
    data = response.json()

    article_url = "https://www.reuters.com" + data["result"]["articles"][0]["canonical_url"]
    title = data["result"]["articles"][0]["title"]
    description = data["result"]["articles"][0]["description"]
    date = data["result"]["articles"][0]["published_time"].split("T")[0]
    try:
        image_url = data["result"]["articles"][0]["thumbnail"]["url"]
    except:
        image_url = "Not Found"

    article_response = requests.get(article_url)
    article_data = article_response.text

    soup = BeautifulSoup(article_data, "html.parser")
    content = soup.find_all("p", {
        "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
    content = [item.text + "\n" for item in content]
    content = "".join(content)
    article = {
        "type": "Aerospace and Defense",
        "article_url": article_url,
        "title": title,
        "date": date,
        "image_url": image_url,
        "description": description,
        "content": content
    }
    pprint.pprint(article)


# ================Media and Telecom=============

def export_media_and_telecom():
    for j in range(2):
        id = f"{9 * j}"
        URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22id%22%3A%22%2Fbusiness%2Fmedia-telecom%2F%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Fmedia-telecom%2F%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22*%22%2C%22sophi_widget%22%3A%22topic%22%2C%22uri%22%3A%22%2Fbusiness%2Fmedia-telecom%2F%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
        headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

        response = requests.get(url=URL, headers=headers)
        data = response.json()

        for i in range(len(data["result"]["articles"])):
            article_url = "https://www.reuters.com" + data["result"]["articles"][i]["canonical_url"]
            title = data["result"]["articles"][i]["title"].replace("'", "").replace(",", " ")
            description = data["result"]["articles"][i]["description"].replace("'", "").replace(",", " ")
            date = data["result"]["articles"][i]["published_time"].split("T")[0]
            try:
                image_url = data["result"]["articles"][i]["thumbnail"]["url"]
            except:
                image_url = "Not Found"

            article_response = requests.get(article_url)
            article_data = article_response.text

            soup = BeautifulSoup(article_data, "html.parser")
            content = soup.find_all("p", {
                "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
            content = [item.text + "\n" for item in content]
            content = "".join(content).replace("'", "").replace(",", " ")

            with open('media and telecom.csv', 'a', newline='', encoding="UTF-8") as file:
                writer_object = writer(file)
                try:
                    new_row = [article_url, title, date, image_url, description, content]
                except:
                    pass
                writer_object.writerow(new_row)
            file.close()


def get_media_and_telecom():
    id = "0"
    URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22id%22%3A%22%2Fbusiness%2Fmedia-telecom%2F%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Fmedia-telecom%2F%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22*%22%2C%22sophi_widget%22%3A%22topic%22%2C%22uri%22%3A%22%2Fbusiness%2Fmedia-telecom%2F%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
    headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

    response = requests.get(url=URL, headers=headers)
    data = response.json()

    article_url = "https://www.reuters.com" + data["result"]["articles"][0]["canonical_url"]
    title = data["result"]["articles"][0]["title"]
    description = data["result"]["articles"][0]["description"]
    date = data["result"]["articles"][0]["published_time"].split("T")[0]
    try:
        image_url = data["result"]["articles"][0]["thumbnail"]["url"]
    except:
        image_url = "Not Found"

    article_response = requests.get(article_url)
    article_data = article_response.text

    soup = BeautifulSoup(article_data, "html.parser")
    content = soup.find_all("p", {
        "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
    content = [item.text + "\n" for item in content]
    content = "".join(content)
    article = {
        "type": "Aerospace and Defense",
        "article_url": article_url,
        "title": title,
        "date": date,
        "image_url": image_url,
        "description": description,
        "content": content
    }
    pprint.pprint(article)


# ================Retail and Consumer==========

def export_retail_and_consumer():
    for j in range(2):
        id = f"{9 * j}"
        URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22id%22%3A%22%2Fbusiness%2Fretail-consumer%2F%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Fretail-consumer%2F%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22*%22%2C%22sophi_widget%22%3A%22topic%22%2C%22uri%22%3A%22%2Fbusiness%2Fretail-consumer%2F%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
        headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

        response = requests.get(url=URL, headers=headers)
        data = response.json()

        for i in range(len(data["result"]["articles"])):
            article_url = "https://www.reuters.com" + data["result"]["articles"][i]["canonical_url"]
            title = data["result"]["articles"][i]["title"].replace("'", "").replace(",", " ")
            description = data["result"]["articles"][i]["description"].replace("'", "").replace(",", " ")
            date = data["result"]["articles"][i]["published_time"].split("T")[0]
            try:
                image_url = data["result"]["articles"][i]["thumbnail"]["url"]
            except:
                image_url = "Not Found"

            article_response = requests.get(article_url)
            article_data = article_response.text

            soup = BeautifulSoup(article_data, "html.parser")
            content = soup.find_all("p", {
                "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
            content = [item.text + "\n" for item in content]
            content = "".join(content).replace("'", "").replace(",", " ")

            with open('Retail and consumer.csv', 'a', newline='', encoding="UTF-8") as file:
                writer_object = writer(file)
                try:
                    new_row = [article_url, title, date, image_url, description, content]
                except:
                    pass
                writer_object.writerow(new_row)
            file.close()


def get_retail_and_consumer():
    id = "0"
    URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22id%22%3A%22%2Fbusiness%2Fretail-consumer%2F%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Fretail-consumer%2F%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22*%22%2C%22sophi_widget%22%3A%22topic%22%2C%22uri%22%3A%22%2Fbusiness%2Fretail-consumer%2F%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
    headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

    response = requests.get(url=URL, headers=headers)
    data = response.json()

    article_url = "https://www.reuters.com" + data["result"]["articles"][0]["canonical_url"]
    title = data["result"]["articles"][0]["title"]
    description = data["result"]["articles"][0]["description"]
    date = data["result"]["articles"][0]["published_time"].split("T")[0]
    try:
        image_url = data["result"]["articles"][0]["thumbnail"]["url"]
    except:
        image_url = "Not Found"

    article_response = requests.get(article_url)
    article_data = article_response.text

    soup = BeautifulSoup(article_data, "html.parser")
    content = soup.find_all("p", {
        "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
    content = [item.text + "\n" for item in content]
    content = "".join(content)
    article = {
        "type": "Aerospace and Defense",
        "article_url": article_url,
        "title": title,
        "date": date,
        "image_url": image_url,
        "description": description,
        "content": content
    }
    pprint.pprint(article)


# ==================Charged======================

def export_charged():
    for j in range(2):
        id = f"{9 * j}"
        URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Fcharged%2F%22%2C%22section_optional_fields%22%3A%22all%22%2C%22size%22%3A9%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
        headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

        response = requests.get(url=URL, headers=headers)
        data = response.json()

        for i in range(len(data["result"]["articles"])):
            article_url = "https://www.reuters.com" + data["result"]["articles"][i]["canonical_url"]
            title = data["result"]["articles"][i]["title"].replace("'", "").replace(",", " ")
            description = data["result"]["articles"][i]["description"].replace("'", "").replace(",", " ")
            date = data["result"]["articles"][i]["published_time"].split("T")[0]
            try:
                image_url = data["result"]["articles"][i]["thumbnail"]["url"]
            except:
                image_url = "Not Found"

            article_response = requests.get(article_url)
            article_data = article_response.text

            soup = BeautifulSoup(article_data, "html.parser")
            content = soup.find_all("p", {
                "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
            content = [item.text + "\n" for item in content]
            content = "".join(content).replace("'", "").replace(",", " ")

            with open('Charged.csv', 'a', newline='', encoding="UTF-8") as file:
                writer_object = writer(file)
                try:
                    new_row = [article_url, title, date, image_url, description, content]
                except:
                    pass
                writer_object.writerow(new_row)
            file.close()


def get_charged():
    id = "0"
    URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Fcharged%2F%22%2C%22section_optional_fields%22%3A%22all%22%2C%22size%22%3A9%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
    headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

    response = requests.get(url=URL, headers=headers)
    data = response.json()

    article_url = "https://www.reuters.com" + data["result"]["articles"][0]["canonical_url"]
    title = data["result"]["articles"][0]["title"]
    description = data["result"]["articles"][0]["description"]
    date = data["result"]["articles"][0]["published_time"].split("T")[0]
    try:
        image_url = data["result"]["articles"][0]["thumbnail"]["url"]
    except:
        image_url = "Not Found"

    article_response = requests.get(article_url)
    article_data = article_response.text

    soup = BeautifulSoup(article_data, "html.parser")
    content = soup.find_all("p", {
        "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
    content = [item.text + "\n" for item in content]
    content = "".join(content)
    article = {
        "type": "Aerospace and Defense",
        "article_url": article_url,
        "title": title,
        "date": date,
        "image_url": image_url,
        "description": description,
        "content": content
    }
    pprint.pprint(article)


# ============future-of-money================

def export_future_of_money():
    for j in range(2):
        id = f"{9 * j}"
        URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Ffuture-of-money%2F%22%2C%22section_optional_fields%22%3A%22all%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22home%22%2C%22sophi_widget%22%3A%22future_of_money%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"

        headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

        response = requests.get(url=URL, headers=headers)
        data = response.json()

        for i in range(len(data["result"]["articles"])):
            article_url = "https://www.reuters.com" + data["result"]["articles"][i]["canonical_url"]
            title = data["result"]["articles"][i]["title"].replace("'", "").replace(",", " ")
            description = data["result"]["articles"][i]["description"].replace("'", "").replace(",", " ")
            date = data["result"]["articles"][i]["published_time"].split("T")[0]
            image_url = data["result"]["articles"][i]["thumbnail"]["url"]

            article_response = requests.get(article_url)
            article_data = article_response.text

            soup = BeautifulSoup(article_data, "html.parser")
            content = soup.find_all("p", {
                "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
            content = [item.text + "\n" for item in content]
            content = "".join(content).replace("'", "").replace(",", " ")

            with open('future-of-money.csv', 'a', newline='', encoding="UTF-8") as file:
                writer_object = writer(file)
                try:
                    new_row = [article_url, title, date, image_url, description, content]
                except:
                    pass
                writer_object.writerow(new_row)
            file.close()


def get_future_of_money():
    id = "0"
    URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Ffuture-of-money%2F%22%2C%22section_optional_fields%22%3A%22all%22%2C%22size%22%3A9%2C%22sophi_page%22%3A%22home%22%2C%22sophi_widget%22%3A%22future_of_money%22%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
    headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

    response = requests.get(url=URL, headers=headers)
    data = response.json()

    article_url = "https://www.reuters.com" + data["result"]["articles"][0]["canonical_url"]
    title = data["result"]["articles"][0]["title"]
    description = data["result"]["articles"][0]["description"]
    date = data["result"]["articles"][0]["published_time"].split("T")[0]
    try:
        image_url = data["result"]["articles"][0]["thumbnail"]["url"]
    except:
        image_url = "Not Found"

    article_response = requests.get(article_url)
    article_data = article_response.text

    soup = BeautifulSoup(article_data, "html.parser")
    content = soup.find_all("p", {
        "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
    content = [item.text + "\n" for item in content]
    content = "".join(content)
    article = {
        "type": "Aerospace and Defense",
        "article_url": article_url,
        "title": title,
        "date": date,
        "image_url": image_url,
        "description": description,
        "content": content
    }
    pprint.pprint(article)


# ============future-of-health================

def export_future_of_health():
    for j in range(2):
        id = f"{9 * j}"
        URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Ffuture-of-health%2F%22%2C%22section_optional_fields%22%3A%22all%22%2C%22size%22%3A9%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
        headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

        response = requests.get(url=URL, headers=headers)
        data = response.json()

        for i in range(len(data["result"]["articles"])):
            article_url = "https://www.reuters.com" + data["result"]["articles"][i]["canonical_url"]
            title = data["result"]["articles"][i]["title"].replace("'", "").replace(",", " ")
            description = data["result"]["articles"][i]["description"].replace("'", "").replace(",", " ")
            date = data["result"]["articles"][i]["published_time"].split("T")[0]
            image_url = data["result"]["articles"][i]["thumbnail"]["url"]

            article_response = requests.get(article_url)
            article_data = article_response.text

            soup = BeautifulSoup(article_data, "html.parser")
            content = soup.find_all("p", {
                "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
            content = [item.text + "\n" for item in content]
            content = "".join(content).replace("'", "").replace(",", " ")

            with open('future-of-health.csv', 'a', newline='', encoding="UTF-8") as file:
                writer_object = writer(file)
                try:
                    new_row = [article_url, title, date, image_url, description, content]
                except:
                    pass
                writer_object.writerow(new_row)
            file.close()


def get_future_of_health():
    id = "0"
    URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Ffuture-of-health%2F%22%2C%22section_optional_fields%22%3A%22all%22%2C%22size%22%3A9%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
    headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

    response = requests.get(url=URL, headers=headers)
    data = response.json()

    article_url = "https://www.reuters.com" + data["result"]["articles"][0]["canonical_url"]
    title = data["result"]["articles"][0]["title"]
    description = data["result"]["articles"][0]["description"]
    date = data["result"]["articles"][0]["published_time"].split("T")[0]
    try:
        image_url = data["result"]["articles"][0]["thumbnail"]["url"]
    except:
        image_url = "Not Found"

    article_response = requests.get(article_url)
    article_data = article_response.text

    soup = BeautifulSoup(article_data, "html.parser")
    content = soup.find_all("p", {
        "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
    content = [item.text + "\n" for item in content]
    content = "".join(content)
    article = {
        "type": "Aerospace and Defense",
        "article_url": article_url,
        "title": title,
        "date": date,
        "image_url": image_url,
        "description": description,
        "content": content
    }
    pprint.pprint(article)


# ============take-five================

def export_take_five():
    for j in range(2):
        id = f"{9 * j}"
        URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Ftake-five%2F%22%2C%22section_optional_fields%22%3Anull%2C%22size%22%3A9%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
        headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

        response = requests.get(url=URL, headers=headers)
        data = response.json()

        for i in range(len(data["result"]["articles"])):
            article_url = "https://www.reuters.com" + data["result"]["articles"][i]["canonical_url"]
            title = data["result"]["articles"][i]["title"].replace("'", "").replace(",", " ")
            description = data["result"]["articles"][i]["description"].replace("'", "").replace(",", " ")
            date = data["result"]["articles"][i]["published_time"].split("T")[0]
            image_url = data["result"]["articles"][i]["thumbnail"]["url"]

            article_response = requests.get(article_url)
            article_data = article_response.text

            soup = BeautifulSoup(article_data, "html.parser")
            content = soup.find_all("p", {
                "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
            content = [item.text + "\n" for item in content]
            content = "".join(content).replace("'", "").replace(",", " ")

            with open('take-five.csv', 'a', newline='', encoding="UTF-8") as file:
                writer_object = writer(file)
                try:
                    new_row = [article_url, title, date, image_url, description, content]
                except:
                    pass
                writer_object.writerow(new_row)
            file.close()


def get_take_five():
    id = "0"
    URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Ftake-five%2F%22%2C%22section_optional_fields%22%3Anull%2C%22size%22%3A9%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
    headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

    response = requests.get(url=URL, headers=headers)
    data = response.json()

    article_url = "https://www.reuters.com" + data["result"]["articles"][0]["canonical_url"]
    title = data["result"]["articles"][0]["title"]
    description = data["result"]["articles"][0]["description"]
    date = data["result"]["articles"][0]["published_time"].split("T")[0]
    try:
        image_url = data["result"]["articles"][0]["thumbnail"]["url"]
    except:
        image_url = "Not Found"

    article_response = requests.get(article_url)
    article_data = article_response.text

    soup = BeautifulSoup(article_data, "html.parser")
    content = soup.find_all("p", {
        "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
    content = [item.text + "\n" for item in content]
    content = "".join(content)
    article = {
        "type": "Aerospace and Defense",
        "article_url": article_url,
        "title": title,
        "date": date,
        "image_url": image_url,
        "description": description,
        "content": content
    }
    pprint.pprint(article)


# =============reuters-impact=================

def export_reuters_impact():
    for j in range(2):
        id = f"{9 * j}"
        URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Freuters-impact%2F%22%2C%22size%22%3A9%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
        headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

        response = requests.get(url=URL, headers=headers)
        data = response.json()

        for i in range(len(data["result"]["articles"])):
            article_url = "https://www.reuters.com" + data["result"]["articles"][i]["canonical_url"]
            title = data["result"]["articles"][i]["title"].replace("'", "").replace(",", " ")
            description = data["result"]["articles"][i]["description"].replace("'", "").replace(",", " ")
            date = data["result"]["articles"][i]["published_time"].split("T")[0]
            image_url = data["result"]["articles"][i]["thumbnail"]["url"]

            article_response = requests.get(article_url)
            article_data = article_response.text

            soup = BeautifulSoup(article_data, "html.parser")
            content = soup.find_all("p", {
                "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
            content = [item.text + "\n" for item in content]
            content = "".join(content).replace("'", "").replace(",", " ")

            with open('reuters-impact.csv', 'a', newline='', encoding="UTF-8") as file:
                writer_object = writer(file)
                try:
                    new_row = [article_url, title, date, image_url, description, content]
                except:
                    pass
                writer_object.writerow(new_row)
            file.close()


def get_reuters_impact():
    id = "0"
    URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Freuters-impact%2F%22%2C%22size%22%3A9%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
    headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

    response = requests.get(url=URL, headers=headers)
    data = response.json()

    article_url = "https://www.reuters.com" + data["result"]["articles"][0]["canonical_url"]
    title = data["result"]["articles"][0]["title"]
    description = data["result"]["articles"][0]["description"]
    date = data["result"]["articles"][0]["published_time"].split("T")[0]
    try:
        image_url = data["result"]["articles"][0]["thumbnail"]["url"]
    except:
        image_url = "Not Found"

    article_response = requests.get(article_url)
    article_data = article_response.text

    soup = BeautifulSoup(article_data, "html.parser")
    content = soup.find_all("p", {
        "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
    content = [item.text + "\n" for item in content]
    content = "".join(content)
    article = {
        "type": "Aerospace and Defense",
        "article_url": article_url,
        "title": title,
        "date": date,
        "image_url": image_url,
        "description": description,
        "content": content
    }
    pprint.pprint(article)


# ===============world-at-work====================

def export_world_at_work():
    for j in range(2):
        id = f"{9 * j}"
        URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Fworld-at-work%2F%22%2C%22section_optional_fields%22%3A%22all%22%2C%22size%22%3A9%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
        headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

        response = requests.get(url=URL, headers=headers)
        data = response.json()

        for i in range(len(data["result"]["articles"])):
            article_url = "https://www.reuters.com" + data["result"]["articles"][i]["canonical_url"]
            title = data["result"]["articles"][i]["title"].replace("'", "").replace(",", " ")
            description = data["result"]["articles"][i]["description"].replace("'", "").replace(",", " ")
            date = data["result"]["articles"][i]["published_time"].split("T")[0]
            image_url = data["result"]["articles"][i]["thumbnail"]["url"]

            article_response = requests.get(article_url)
            article_data = article_response.text

            soup = BeautifulSoup(article_data, "html.parser")
            content = soup.find_all("p", {
                "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
            content = [item.text + "\n" for item in content]
            content = "".join(content).replace("'", "").replace(",", " ")

            with open('world-at-work.csv', 'a', newline='', encoding="UTF-8") as file:
                writer_object = writer(file)
                try:
                    new_row = [article_url, title, date, image_url, description, content]
                except:
                    pass
                writer_object.writerow(new_row)
            file.close()


def get_world_at_work():
    id = "0"
    URL = f"https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22arc-site%22%3A%22reuters%22%2C%22called_from_a_component%22%3Atrue%2C%22fetch_type%22%3A%22collection%22%2C%22offset%22%3A{id}%2C%22section_id%22%3A%22%2Fbusiness%2Fworld-at-work%2F%22%2C%22section_optional_fields%22%3A%22all%22%2C%22size%22%3A9%2C%22website%22%3A%22reuters%22%7D&d=122&_website=reuters"
    headers = {'cookie': "reuters-geo=%7B%22country%22%3A%22MA%22%2C%20%22region%22%3A%22-%22%7D"}

    response = requests.get(url=URL, headers=headers)
    data = response.json()

    article_url = "https://www.reuters.com" + data["result"]["articles"][0]["canonical_url"]
    title = data["result"]["articles"][0]["title"]
    description = data["result"]["articles"][0]["description"]
    date = data["result"]["articles"][0]["published_time"].split("T")[0]
    try:
        image_url = data["result"]["articles"][0]["thumbnail"]["url"]
    except:
        image_url = "Not Found"

    article_response = requests.get(article_url)
    article_data = article_response.text

    soup = BeautifulSoup(article_data, "html.parser")
    content = soup.find_all("p", {
        "class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__full_width__ekUdw body__large_body__FV5_X article-body__element__2p5pI"})
    content = [item.text + "\n" for item in content]
    content = "".join(content)
    article = {
        "type": "Aerospace and Defense",
        "article_url": article_url,
        "title": title,
        "date": date,
        "image_url": image_url,
        "description": description,
        "content": content
    }
    pprint.pprint(article)

# ===================================RUN FUNCTIONS====================================
