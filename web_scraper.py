import os
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv

load_dotenv()

s = Service(os.getenv("CHROME_DRIVER_FILE_PATH"))
driver = webdriver.Chrome(service=s)
driver.get("https://ufc.com/events/")
results = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for element in soup.findAll(attrs='events-lastnext events-lastnext--with-countdown'):
    nextEvent = element.find("a");
    if nextEvent not in results:
        results.append(nextEvent)

print(results)