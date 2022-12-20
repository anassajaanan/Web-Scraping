from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from csv import writer
import pandas as pd
import pprint
import time

# ================config====================
op = Options()
op.add_extension('config/pay.crx')
op.add_extension('config/uorigin.crx')
op.add_extension('config/cockies.crx')
PATH = 'config/chromedriver.exe'
cc = DesiredCapabilities.CHROME
cc["pageLoadStrategy"] = "none"


# ===================================Decentralized Finance=============================================
def export_decentralized_finance():
    # ==============Driver===============================
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    Decentralized_Finance_URL = "https://www.bloomberg.com/crypto/defi?srnd=cryptocurrencies-v2"
    driver.get(Decentralized_Finance_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-package-module__story__headline')))
    time.sleep(1)

    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)

    time.sleep(2)

    images = driver.find_elements(By.CLASS_NAME, 'bb-lazy-img__image')
    links = driver.find_elements(By.CLASS_NAME, 'story-package-module__story__headline')

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [title.find_element(By.TAG_NAME, 'a').get_attribute('href') for title in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.CLASS_NAME, 'paywall')))
        driver.implicitly_wait(2)
        w.until(EC.presence_of_element_located((By.CLASS_NAME, 'headline__699ae8fb')))
        title = driver.find_element(By.CLASS_NAME, 'headline__699ae8fb').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'author__619cf27c').find_element(By.TAG_NAME, 'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'pillar__a08f2d74').text
        except:
            type = "Not Found"

        def get_text(input):
            try:
                return str(input.text) + "\n"
            except:
                pass

        content1 = driver.find_element(By.CLASS_NAME, 'body-content').find_elements(By.TAG_NAME, 'p')
        content1 = [get_text(item) for item in content1]
        content2 = driver.find_elements(By.CLASS_NAME, 'paywall')
        content2 = [item.text + "\n" for item in content2]

        content = content1 + content2
        content = "".join(content)

        with open('decentralized-finance.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_decentralized_finance():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    Decentralized_Finance_URL = "https://www.bloomberg.com/crypto/defi?srnd=cryptocurrencies-v2"
    driver.get(Decentralized_Finance_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-package-module__story__headline')))
    time.sleep(1)

    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)

    time.sleep(1)

    articles_imgs = driver.find_element(By.CLASS_NAME, 'bb-lazy-img__image').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'story-package-module__story__headline').find_element(
        By.TAG_NAME, 'a').get_attribute('href')
    time.sleep(2)
    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'paywall')))
    driver.implicitly_wait(2)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'headline__699ae8fb')))
    title = driver.find_element(By.CLASS_NAME, 'headline__699ae8fb').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'author__619cf27c').find_element(By.TAG_NAME, 'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'pillar__a08f2d74').text
    except:
        type = "Not Found"

    def get_text(input):
        try:
            return str(input.text) + "\n"
        except:
            pass

    content1 = driver.find_element(By.CLASS_NAME, 'body-content').find_elements(By.TAG_NAME, 'p')
    content1 = [get_text(item) for item in content1]
    content2 = driver.find_elements(By.CLASS_NAME, 'paywall')
    content2 = [item.text + "\n" for item in content2]

    content = content1 + content2
    content = "".join(content)

    article = {
        "article-type": type,
        "article-link": articles_links,
        "article-title": title,
        "article-img": articles_imgs,
        "article-author": author,
        "date": date,
        "article-content": content,
    }
    pprint.pprint(article)


# ==========================================NFTs===================================================
def export_nfts():
    # ==============Driver===============================
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    NFTS_URL = "https://www.bloomberg.com/crypto/nft?srnd=crypto-defi"
    driver.get(NFTS_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-package-module__story__headline')))
    time.sleep(1)

    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)

    time.sleep(2)

    images = driver.find_elements(By.CLASS_NAME, 'bb-lazy-img__image')
    links = driver.find_elements(By.CLASS_NAME, 'story-package-module__story__headline')

    articles_imgs = [image.get_attribute('src').replace("25x19.jpg", "500x500.jpg") for image in images]
    articles_links = [title.find_element(By.TAG_NAME, 'a').get_attribute('href') for title in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        driver.implicitly_wait(1)
        w.until(EC.presence_of_element_located((By.CLASS_NAME, 'paywall')))
        driver.implicitly_wait(2)
        w.until(EC.presence_of_element_located((By.CLASS_NAME, 'headline__699ae8fb')))

        title = driver.find_element(By.CLASS_NAME, 'headline__699ae8fb').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'author__619cf27c').find_element(By.TAG_NAME, 'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'pillar__a08f2d74').text
        except:
            type = "Not Found"

        def get_text(input):
            try:
                return str(input.text) + "\n"
            except:
                pass

        content1 = driver.find_element(By.CLASS_NAME, 'body-content').find_elements(By.TAG_NAME, 'p')
        content1 = [get_text(item) for item in content1]
        content2 = driver.find_elements(By.CLASS_NAME, 'paywall')
        content2 = [item.text + "\n" for item in content2]

        content = content1 + content2
        content = "".join(content)

        with open('nfts.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_nfts():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    NFTS_URL = "https://www.bloomberg.com/crypto/nft?srnd=crypto-defi"
    driver.get(NFTS_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-package-module__story__headline')))
    time.sleep(1)

    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)

    time.sleep(1)

    articles_imgs = driver.find_element(By.CLASS_NAME, 'bb-lazy-img__image').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'story-package-module__story__headline').find_element(
        By.TAG_NAME, 'a').get_attribute('href')
    time.sleep(2)
    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'paywall')))
    driver.implicitly_wait(2)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'headline__699ae8fb')))
    title = driver.find_element(By.CLASS_NAME, 'headline__699ae8fb').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'author__619cf27c').find_element(By.TAG_NAME, 'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'pillar__a08f2d74').text
    except:
        type = "Not Found"

    def get_text(input):
        try:
            return str(input.text) + "\n"
        except:
            pass

    content1 = driver.find_element(By.CLASS_NAME, 'body-content').find_elements(By.TAG_NAME, 'p')
    content1 = [get_text(item) for item in content1]
    content2 = driver.find_elements(By.CLASS_NAME, 'paywall')
    content2 = [item.text + "\n" for item in content2]

    content = content1 + content2
    content = "".join(content)

    article = {
        "article-type": type,
        "article-link": articles_links,
        "article-title": title,
        "article-img": articles_imgs,
        "article-author": author,
        "date": date,
        "article-content": content,
    }
    pprint.pprint(article)


# ================================================Regulation=================================================
def export_regulation():
    # ==============Driver===============================
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    REGULATION_URL = "https://www.bloomberg.com/crypto/regulation?srnd=crypto-nft"
    driver.get(REGULATION_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-package-module__story__headline')))
    time.sleep(1)

    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)

    time.sleep(2)

    images = driver.find_elements(By.CLASS_NAME, 'bb-lazy-img__image')
    links = driver.find_elements(By.CLASS_NAME, 'story-package-module__story__headline')

    articles_imgs = [image.get_attribute('src').replace("25x19.jpg", "500x500.jpg") for image in images]
    articles_links = [title.find_element(By.TAG_NAME, 'a').get_attribute('href') for title in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        driver.implicitly_wait(1)
        w.until(EC.presence_of_element_located((By.CLASS_NAME, 'paywall')))
        driver.implicitly_wait(2)
        w.until(EC.presence_of_element_located((By.CLASS_NAME, 'headline__699ae8fb')))

        title = driver.find_element(By.CLASS_NAME, 'headline__699ae8fb').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'author__619cf27c').find_element(By.TAG_NAME, 'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'pillar__a08f2d74').text
        except:
            type = "Not Found"

        def get_text(input):
            try:
                return str(input.text) + "\n"
            except:
                pass

        content1 = driver.find_element(By.CLASS_NAME, 'body-content').find_elements(By.TAG_NAME, 'p')
        content1 = [get_text(item) for item in content1]
        content2 = driver.find_elements(By.CLASS_NAME, 'paywall')
        content2 = [item.text + "\n" for item in content2]

        content = content1 + content2
        content = "".join(content)

        with open('regulation.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_regulation():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    REGULATION_URL = "https://www.bloomberg.com/crypto/regulation?srnd=crypto-nft"
    driver.get(REGULATION_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-package-module__story__headline')))
    time.sleep(1)

    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)

    time.sleep(1)

    articles_imgs = driver.find_element(By.CLASS_NAME, 'bb-lazy-img__image').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'story-package-module__story__headline').find_element(
        By.TAG_NAME, 'a').get_attribute('href')
    time.sleep(2)
    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'paywall')))
    driver.implicitly_wait(2)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'headline__699ae8fb')))
    title = driver.find_element(By.CLASS_NAME, 'headline__699ae8fb').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'author__619cf27c').find_element(By.TAG_NAME, 'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'pillar__a08f2d74').text
    except:
        type = "Not Found"

    def get_text(input):
        try:
            return str(input.text) + "\n"
        except:
            pass

    content1 = driver.find_element(By.CLASS_NAME, 'body-content').find_elements(By.TAG_NAME, 'p')
    content1 = [get_text(item) for item in content1]
    content2 = driver.find_elements(By.CLASS_NAME, 'paywall')
    content2 = [item.text + "\n" for item in content2]

    content = content1 + content2
    content = "".join(content)

    article = {
        "article-type": type,
        "article-link": articles_links,
        "article-title": title,
        "article-img": articles_imgs,
        "article-author": author,
        "date": date,
        "article-content": content,
    }
    pprint.pprint(article)


# ===============================================Technology================================================
def export_technology():
    # ==============Driver===============================
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    TECH_URL = "https://www.bloomberg.com/crypto/technology?srnd=crypto-regulation"
    driver.get(TECH_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-package-module__story__headline')))
    time.sleep(1)

    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)

    time.sleep(2)

    images = driver.find_elements(By.CLASS_NAME, 'bb-lazy-img__image')
    links = driver.find_elements(By.CLASS_NAME, 'story-package-module__story__headline')

    articles_imgs = [image.get_attribute('src').replace("25x19.jpg", "500x500.jpg") for image in images]
    articles_links = [title.find_element(By.TAG_NAME, 'a').get_attribute('href') for title in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        driver.implicitly_wait(1)
        w.until(EC.presence_of_element_located((By.CLASS_NAME, 'paywall')))
        driver.implicitly_wait(2)
        w.until(EC.presence_of_element_located((By.CLASS_NAME, 'headline__699ae8fb')))

        title = driver.find_element(By.CLASS_NAME, 'headline__699ae8fb').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'author__619cf27c').find_element(By.TAG_NAME, 'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'pillar__a08f2d74').text
        except:
            type = "Not Found"

        def get_text(input):
            try:
                return str(input.text) + "\n"
            except:
                pass

        content1 = driver.find_element(By.CLASS_NAME, 'body-content').find_elements(By.TAG_NAME, 'p')
        content1 = [get_text(item) for item in content1]
        content2 = driver.find_elements(By.CLASS_NAME, 'paywall')
        content2 = [item.text + "\n" for item in content2]

        content = content1 + content2
        content = "".join(content)

        with open('technology.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, articles_imgs[i], author, date, type, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_technology():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    TECH_URL = "https://www.bloomberg.com/crypto/technology?srnd=crypto-regulation"
    driver.get(TECH_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-package-module__story__headline')))
    time.sleep(1)

    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)

    time.sleep(1)

    articles_imgs = driver.find_element(By.CLASS_NAME, 'bb-lazy-img__image').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'story-package-module__story__headline').find_element(
        By.TAG_NAME, 'a').get_attribute('href')
    time.sleep(2)
    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'paywall')))
    driver.implicitly_wait(2)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'headline__699ae8fb')))
    title = driver.find_element(By.CLASS_NAME, 'headline__699ae8fb').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'author__619cf27c').find_element(By.TAG_NAME, 'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'pillar__a08f2d74').text
    except:
        type = "Not Found"

    def get_text(input):
        try:
            return str(input.text) + "\n"
        except:
            pass

    content1 = driver.find_element(By.CLASS_NAME, 'body-content').find_elements(By.TAG_NAME, 'p')
    content1 = [get_text(item) for item in content1]
    content2 = driver.find_elements(By.CLASS_NAME, 'paywall')
    content2 = [item.text + "\n" for item in content2]

    content = content1 + content2
    content = "".join(content)

    article = {
        "article-type": type,
        "article-link": articles_links,
        "article-title": title,
        "article-img": articles_imgs,
        "article-author": author,
        "date": date,
        "article-content": content,
    }
    pprint.pprint(article)


# ============================================CRYPTO==================================================
def export_crypto():
    # ==============Driver===============================
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    CRYPTO_URL = "https://www.bloomberg.com/crypto"
    driver.get(CRYPTO_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-list-story__info__headline')))
    time.sleep(1)

    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)

    time.sleep(2)

    # images = driver.find_elements(By.CLASS_NAME, 'bb-lazy-img__image')
    links = driver.find_elements(By.CLASS_NAME, 'story-list-story__info__headline-link')

    # articles_imgs = [image.get_attribute('src').replace("25x19.jpg", "500x500.jpg") for image in images]
    articles_links = [title.get_attribute('href') for title in links]

    # print(articles_imgs)
    # print(articles_links)

    time.sleep(2)

    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        driver.implicitly_wait(1)
        w.until(EC.presence_of_element_located((By.CLASS_NAME, 'paywall')))
        driver.implicitly_wait(2)
        w.until(EC.presence_of_element_located((By.CLASS_NAME, 'headline__2a7f6bea')))

        title = driver.find_element(By.CLASS_NAME, 'headline__2a7f6bea').text
        try:
            author = driver.find_element(By.CLASS_NAME, 'author__619cf27c').find_element(By.TAG_NAME, 'a').text
        except:
            author = "Not Found"
        date = driver.find_element(By.TAG_NAME, 'time').text
        try:
            type = driver.find_element(By.CLASS_NAME, 'brand__3ac459ef').text
        except:
            type = "Not Found"

        def get_text(input):
            try:
                return str(input.text) + "\n"
            except:
                pass

        content1 = driver.find_element(By.CLASS_NAME, 'body-content').find_elements(By.TAG_NAME, 'p')
        content1 = [get_text(item) for item in content1]
        content2 = driver.find_elements(By.CLASS_NAME, 'paywall')
        content2 = [item.text + "\n" for item in content2]

        content = content1 + content2
        content = "".join(content)

        with open('crypto.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], title, author, date, type, content]
            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_crypto():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    CRYPTO_URL = "https://www.bloomberg.com/crypto"
    driver.get(CRYPTO_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'story-package-module__story__headline')))
    time.sleep(1)

    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)

    time.sleep(1)

    articles_links = driver.find_element(By.CLASS_NAME, 'story-package-module__story__headline').find_element(
        By.TAG_NAME, 'a').get_attribute('href')
    time.sleep(2)
    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'paywall')))
    driver.implicitly_wait(2)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'headline__699ae8fb')))
    title = driver.find_element(By.CLASS_NAME, 'headline__699ae8fb').text
    try:
        author = driver.find_element(By.CLASS_NAME, 'author__619cf27c').find_element(By.TAG_NAME, 'a').text
    except:
        author = "Not Found"
    date = driver.find_element(By.TAG_NAME, 'time').text
    try:
        type = driver.find_element(By.CLASS_NAME, 'pillar__a08f2d74').text
    except:
        type = "Not Found"

    def get_text(input):
        try:
            return str(input.text) + "\n"
        except:
            pass

    content1 = driver.find_element(By.CLASS_NAME, 'body-content').find_elements(By.TAG_NAME, 'p')
    content1 = [get_text(item) for item in content1]
    content2 = driver.find_elements(By.CLASS_NAME, 'paywall')
    content2 = [item.text + "\n" for item in content2]

    content = content1 + content2
    content = "".join(content)

    article = {
        "article-type": type,
        "article-link": articles_links,
        "article-title": title,
        "article-author": author,
        "date": date,
        "article-content": content,
    }
    pprint.pprint(article)

# ==============================================FINISH======================================================

# ===========================================RUN function========================================================
