from selenium import webdriver
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver=webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

from selenium.webdriver.common.keys import Keys
import os
os.system("chmod +x chromedriver")
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.python.org")
#driver.get("https://www.google.com")

print(driver.title)

search_bar = driver.find_element_by_name("q")

search_bar.clear()

search_bar.send_keys("getting started with python")

search_bar.send_keys(Keys.RETURN)

print(driver.current_url)

driver.close()
