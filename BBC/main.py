from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from csv import writer
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


# ==========================================Cryptocurrency==========================================

def export_cryptocurrency():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    BBC_URL = "https://www.bbc.com/news/topics/cyd7z4rvdm3t"
    driver.get(BBC_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'ssrcss-1j8v9o5-PromoLink')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)

    images = driver.find_elements(By.CLASS_NAME, 'ssrcss-evoj7m-Image')
    links = driver.find_elements(By.CLASS_NAME, 'ssrcss-1j8v9o5-PromoLink')
    titles = driver.find_elements(By.CLASS_NAME, 'ssrcss-17zglt8-PromoHeadline')
    types = driver.find_elements(By.CLASS_NAME, 'ssrcss-ux1pfd-MetadataLink')

    def get_type(element):
        try:
            return element.find_element(By.TAG_NAME, 'span').text
        except:
            return "NOT FOUND"

    articles_imgs = [image.get_attribute('src') for image in images]
    articles_links = [link.get_attribute('href') for link in links]
    articles_titles = [title.find_element(By.TAG_NAME, 'span').text for title in titles]
    articles_types = [get_type(element) for element in types]

    time.sleep(2)

    articles_links = articles_links[:20]
    for i in range(len(articles_links)):
        driver.get(articles_links[i])
        w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(2)
        try:
            author = driver.find_element(By.CLASS_NAME, 'ssrcss-68pt20-Text-TextContributorName').text
        except:
            author = "NOT FOUND"
        try:
            description = driver.find_element(By.CLASS_NAME, 'ssrcss-hmf8ql-BoldText').text
        except:
            description = "NOT FOUND"
        try:
            date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
        except:
            date = "NOT FOUND"

        content = driver.find_elements(By.CLASS_NAME, 'ssrcss-1q0x1qg-Paragraph')
        content = [str(item.text) + "\n" for item in content]
        content = "".join(content)

        time.sleep(2)

        if len(content) == 0:
            content = "This article is Audible"
            description = "This article is Audible"
            author = "This article is Audible"
            date = "This article is Audible"

        with open('cryptocurrency.csv', 'a', newline='', encoding="UTF-8") as file:
            writer_object = writer(file)
            try:
                new_row = [articles_links[i], articles_titles[i], articles_imgs[i], author, date,
                           articles_types[i], description, content]

            except:
                pass
            writer_object.writerow(new_row)
        file.close()
        time.sleep(1)


def get_cryptocurrency():
    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=cc, options=op)
    w = WebDriverWait(driver, 100)
    driver.implicitly_wait(0.5)
    BBC_URL = "https://www.bbc.com/news/topics/cyd7z4rvdm3t"
    driver.get(BBC_URL)
    w.until(EC.presence_of_element_located((By.CLASS_NAME, 'ssrcss-1j8v9o5-PromoLink')))
    time.sleep(2)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()
    driver.switch_to.window(p)
    time.sleep(4)

    def get_type(element):
        try:
            return element.find_element(By.TAG_NAME, 'span').text
        except:
            return "NOT FOUND"

    articles_imgs = driver.find_element(By.CLASS_NAME, 'ssrcss-evoj7m-Image').get_attribute('src')
    articles_links = driver.find_element(By.CLASS_NAME, 'ssrcss-1j8v9o5-PromoLink').get_attribute('href')
    articles_titles = driver.find_element(By.CLASS_NAME, 'ssrcss-17zglt8-PromoHeadline').find_element(By.TAG_NAME,
                                                                                                      'span').text
    articles_types = driver.find_element(By.CLASS_NAME, 'ssrcss-ux1pfd-MetadataLink')
    articles_types = get_type(articles_types)

    time.sleep(2)

    driver.get(articles_links)
    w.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    time.sleep(2)
    try:
        author = driver.find_element(By.CLASS_NAME, 'ssrcss-68pt20-Text-TextContributorName').text
    except:
        author = "NOT FOUND"
    try:
        description = driver.find_element(By.CLASS_NAME, 'ssrcss-hmf8ql-BoldText').text
    except:
        description = "NOT FOUND"
    try:
        date = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime').split("T")[0]
    except:
        date = "NOT FOUND"

    content = driver.find_elements(By.CLASS_NAME, 'ssrcss-1q0x1qg-Paragraph')
    content = [str(item.text) + "\n" for item in content]
    content = "".join(content)

    time.sleep(2)

    if len(content) == 0:
        content = "This article is Audible"
        description = "This article is Audible"
        author = "This article is Audible"
        date = "This article is Audible"

    article = {
        "article-link": articles_links,
        "article-title": articles_titles,
        "article-img": articles_imgs,
        "article-author": author,
        "date": date,
        "article-description": description,
        "article-content": content,
    }
    pprint.pprint(article)

# =====================================RUN FUNCTIONS=============================================
