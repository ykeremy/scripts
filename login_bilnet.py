from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import poplib
import email
import time

#############
# user info #
#############

# BILNET_USERNAME = "to be filled by the user"
# BILNET_PWD = "to be filled by the user"

# TODO: Do not show browser, just print login info.
browser = webdriver.Chrome()
browser.get("https://auth.bilkent.edu.tr/")

# find the elements
try:  # if not logged in
    username = browser.find_element_by_css_selector(
        "[placeholder='Bil-Net ID']")
    password = browser.find_element_by_css_selector(
        "[placeholder='Bil-Net Password']")
    # send the necessary info
    username.send_keys(BILNET_USERNAME)
    password.send_keys(BILNET_PWD)

    # find button and click login
    check = browser.find_element_by_css_selector("[name='agree']")
    check.click()
    button = browser.find_element_by_css_selector(
        "[class='btn btn-lg btn-primary btn-block']")
    button.click()

except NoSuchElementException as e:
    print("Already logged in.")

loginInfo = browser.find_element_by_css_selector(
    "[class='alert alert-info']").text
if 'successful' in loginInfo:
    print(loginInfo)
browser.quit()
