from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import poplib
import email

#############
# user info #
#############

# SRS_USERNAME = "to be filled by the user"
# SRS_PWD = "to be filled by the user"
# MAIL_USERNAME = "to be filled by the user"
# MAIL_PWD = "to be filled by the user"

browser = webdriver.Firefox() 	# for Firefox geckodriver must be in the path of
# your OS. For Chrome or any other modification is necessary.

# go to the login site
browser.get("https://stars.bilkent.edu.tr/srs")

# find the elements
username = browser.find_element_by_css_selector("[id='LoginForm_username']")
password = browser.find_element_by_css_selector("[id^='LoginForm-']")

# send the necessary info
username.send_keys(SRS_USERNAME)
password.send_keys(SRS_PWD)

# find button and click login
button = browser.find_element_by_css_selector("[name='yt0']")
button.click()

in_verif_code = browser.find_element_by_css_selector(
    "[id='EmailVerifyForm_verifyCode']")
button = browser.find_element_by_css_selector("[name='yt0']")

#######################################
# get the verification code from mail #
#######################################

# connect to pop3 server
SERVER_POP3 = "mail.bilkent.edu.tr"
webmail = poplib.POP3_SSL(SERVER_POP3)

# login to webmail
webmail.user(MAIL_USERNAME)
webmail.pass_(MAIL_PWD)

latest_mail_id = webmail.stat()

# latest mail is the mail that contains the verification code
latest_email = webmail.top(latest_mail_id[0], 10)
latest_email = str(latest_email[1])

# parse verification code
# verification starts at 19th index
index = 19 + latest_email.find("Verification Code: ")
verif_code = latest_email[index:index + 5] 		# verification code is 5 digits
print(verif_code)

in_verif_code.send_keys(verif_code)

# find button and click verify
button.click()
