from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("detach", True)

chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# print(driver.page_source)
driver.get("https://www.ufc.com/events")
time.sleep(1);

# cookieNotificationElements = driver.find_element(By.CLASS_NAME, "onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button mobile close-icon");
buttons = driver.find_elements(By.CSS_SELECTOR, '[aria-label="Close Banner Button"]');
buttons[len(buttons) - 1].click();
time.sleep(1);

viewFightCardButtons = driver.find_elements(By.CSS_SELECTOR, "[tabindex='0']");

viewFightCardButtons[0].click();

# print(driver.current_url);
# wait.until(EC.url_changes(driver.current_url))

print(driver.current_url);
# driver.quit()
print("Finished!")