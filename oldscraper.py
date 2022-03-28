from dotenv import load_dotenv
load_dotenv()
import os
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(os.getenv("CHROME_DRIVER_FILE_PATH"))
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=s, options=chrome_options)
# driver.maximize_window()
# driver.get("https://google.com")
driver.get("https://ufc.com/events/")
# driver.get("https://sportsbook.draftkings.com/featured")
# driver.get('https://oxylabs.io/blog')
print(driver.current_url)
cookieConsentCloseElementXPath = "/html[@class=' no-touchevents details js']/body[@class='fontyourface path-events']/div[@id='onetrust-consent-sdk']/div[@id='onetrust-banner-sdk']/div[@class='ot-sdk-container']/div[@class='ot-sdk-row']/div[@id='onetrust-close-btn-container']/a[@class='onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button onetrust-lg close-icon']"
fightCardElementXPath  = "//a[contains(@href, 'ufc.com')]/span"

driver.find_element(By.XPATH, cookieConsentCloseElementXPath).click()
driver.find_element(By.XPATH, fightCardElementXPath).click()
# print("HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
# print(element)
results = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for element in soup.findAll("li", { "class": "l-listing__item"}):
    nextEvent = element
    if nextEvent not in results:
        results.append(nextEvent)

print(len(results))
print(results[0])