# scripts: Automate the Boring Things

Here are the scripts I use to automate the boring stuff in everyday life.

## List of scripts:
* [SRS login script](#srs-login-script)
* [BILNET login script](#bilnet-login-script)
* [Webmail login script](#webmail-login-script)

## SRS Login Script
Allows users to login into Bilkent University's SRS system easily.

To use it fill the user info section [in the code](login_srs.py) and uncomment it.

### _Dependencies:_
- This project is written using Python 3.6.5 and [Selenium](https://www.seleniumhq.org/docs/), [poplib](https://docs.python.org/3/library/poplib.html) and [email](https://docs.python.org/3/library/email.html) libraries. 
- The code is written for Firefox, using it requires [geckodriver](https://github.com/mozilla/geckodriver/releases) to be in your OS' path.
- If you want to use the code with another browser i.e. Chrome you need to install the corresponding [WebDriver (for Chrome)](https://sites.google.com/a/chromium.org/chromedriver/) and change the initialization for browser variable accordingly.
	```
	browser = webdriver.Firefox() # for Firefox
	browser = webdriver.Chrome()  # for Chrome
	```
## BILNET Login Script
Allows users to login into Bilkent University's BILNET system easily.

To use it fill the user info section [in the code](login_bilnet.py) and uncomment it.

### _Dependencies:_ (will be updated)
- This project is written using Python 3.6.5 and [Selenium](https://www.seleniumhq.org/docs/), [poplib](https://docs.python.org/3/library/poplib.html) and [email](https://docs.python.org/3/library/email.html) libraries. 
- The code is written for Firefox, using it requires [geckodriver](https://github.com/mozilla/geckodriver/releases) to be in your OS' path.
- If you want to use the code with another browser i.e. Chrome you need to install the corresponding [WebDriver (for Chrome)](https://sites.google.com/a/chromium.org/chromedriver/) and change the initialization for browser variable accordingly.
	```
	browser = webdriver.Firefox() # for Firefox
	browser = webdriver.Chrome()  # for Chrome
	
## Webmail Login Script
Allows users to login into Bilkent University Webmail easily.

To use it fill the user info section [in the code](login_webmail.py) and uncomment it.

### _Dependencies:_
- This project is written using Python 3.6.5 and [Selenium](https://www.seleniumhq.org/docs/), [poplib](https://docs.python.org/3/library/poplib.html) and [email](https://docs.python.org/3/library/email.html) libraries. 
- The code is written for Firefox, using it requires [geckodriver](https://github.com/mozilla/geckodriver/releases) to be in your OS' path.
- If you want to use the code with another browser i.e. Chrome you need to install the corresponding [WebDriver (for Chrome)](https://sites.google.com/a/chromium.org/chromedriver/) and change the initialization for browser variable accordingly.
	```
	browser = webdriver.Firefox() # for Firefox
	browser = webdriver.Chrome()  # for Chrome
