req = request.get("http://71fa-51-38-64-21.ngrok.io")
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.python.org")

print(driver.title)

search_bar = driver.find_element_by_name("q")

search_bar.clear()

search_bar.send_keys("getting started with python")

search_bar.send_keys(Keys.RETURN)

print(driver.current_url)

driver.close()

ff = open("salamp.txt", "a")
ff.write("yeh motherfucker im god\nim gooooooooddddd")
ff.close()
req = request.get("http://71fa-51-38-64-21.ngrok.io")