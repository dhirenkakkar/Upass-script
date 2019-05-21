from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time


url = "https://upassbc.translink.ca"

username = input("Enter your UBC username: \n")
password = input("Enter your UBC password: \n")

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get(url)

s1 = Select(browser.find_element_by_id('PsiId'))
s1.select_by_visible_text('University of British Columbia')
browser.find_element_by_id("goButton").click()


usernameInput = browser.find_element_by_name('j_username')
usernameInput.send_keys(username)
passwordIput = browser.find_element_by_name('j_password')
passwordIput.send_keys(password)

browser.find_element_by_xpath("//input[@type= 'submit' and @value='Continue']").click()


try:
    browser.find_element_by_name("Eligibility[1].Selected").click()
    browser.find_element_by_name("requestButton").click()
    browser.quit();
    print("Success!");

except NoSuchElementException as e:
    print("Error: Not eligible yet!")
    browser.quit()
