import sys, os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities

address_input = raw_input("Address: ")

chromedriver_location = './assets/chromedriver'
# chrome_options = Options()
# chrome_options.add_argument('--dns-prefetch-disable')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--lang=en-US')

# chrome_prefs = {
#     'intl.accept_languages': 'en-US'
# }
# chrome_options.add_experimental_option('prefs', chrome_prefs)
browser = webdriver.Chrome(chromedriver_location)
browser.implicitly_wait(2)


browser.get(address_input)