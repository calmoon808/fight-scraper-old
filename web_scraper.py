from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("detach", True)

chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=https://discord-stock-moonbot.herokuapp.com/&client_id=C7XQAIY9SREZRXKWVTXMLWF9TMHB3ZP0%40AMER.OAUTHAP")
print(driver.page_source)
wait = WebDriverWait(driver, 10)

usernameInput = driver.find_element(By.ID, "username0");
usernameInput.send_keys("cmoon808")
passwordInput = driver.find_element(By.ID, "password1");
passwordInput.send_keys("ElGaucho08!")
submitButton = driver.find_element(By.ID, "accept");
submitButton.click();
submitButton = driver.find_element(By.ID, "accept");
submitButton.click();

print(driver.current_url);
print("Finished!")