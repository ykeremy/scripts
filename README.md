# Auto-SRS-Login
An automated python script allows the user to login into Bilkent University's SRS system easily.

**SRS:** Student Review System for continuing Bilkent University students and alumni

To use it fill in the currently commented user info section [in the code](login_srs.py) and uncomment it.

### _Notes:_
- This project is written using Python 3.6.5 and [Selenium](https://www.seleniumhq.org/docs/), [poplib](https://docs.python.org/3/library/poplib.html) and [email](https://docs.python.org/3/library/email.html) libraries. 
- The code is written for Firefox, using it requires [geckodriver](https://github.com/mozilla/geckodriver/releases) to be in your OS' path.
- If you want to use the code with another browser i.e. Chrome you need to install the corresponding [WebDriver (for Chrome)](https://sites.google.com/a/chromium.org/chromedriver/) and change the initialization for browser variable accordingly.
	```
	browser = webdriver.Firefox() # for Firefox
	browser = webdriver.Chrome()  # for Chrome
	```
