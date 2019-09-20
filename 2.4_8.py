from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'
driver = webdriver.Chrome()
driver.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100')
)

driver.find_element_by_css_selector('#book').click()

x = driver.find_element_by_css_selector('#input_value').text

result = calc(x)

driver.find_element_by_css_selector('#answer').send_keys(result)

driver.find_element_by_css_selector('#solve').click()

