from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import poplib
import email

#############
# user info #
#############

# MAIL_USERNAME = "to be filled by the user"
# MAIL_PWD = "to be filled by the user"

browser = webdriver.Chrome()  # for Firefox geckodriver must be in the path of
# your OS. For Chrome or any other modification is necessary.

browser.get("https://webmail.bilkent.edu.tr/")

# find the elements
username = browser.find_element_by_css_selector("[id='rcmloginuser']")
password = browser.find_element_by_css_selector("[id^='LoginForm-']")

# send the necessary info
username.send_keys(MAIL_USERNAME)
password.send_keys(MAIL_PWD)

# find button and click login
button = browser.find_element_by_css_selector("[id='rcmloginsubmit']")
button.click()
