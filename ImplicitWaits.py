from selenium import webdriver
browser = webdriver.Chrome()

browser.implicitly_wait(5)

browser.get("https://suninjuly.github.io/cats.html")

button = browser.find_element_by_id("button").button.click()