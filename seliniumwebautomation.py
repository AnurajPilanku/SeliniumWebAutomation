from selenium import webdriver
import time
#import yaml

#conf = yaml.load(open('loginDetails.yml'))
#username= conf['akamiuser']['email']
#password = conf['akamiuser']['password']
url_tobe_cleared='https://www.3m.com/3M/en_US/health-care-us/' #from ITSM description
username="ewcdadmin@mmm.com"
password="Portal-23"
url='https://control.akamai.com/'
userxpath="//input[@name='username']"
passwordxpath='//input[@name="password"]'
xpathNext="//span[@class='text ng-scope']"
signinxpath='//span[@translate="auth.verificationForm.signInBtnText"]'
skipxpath="//span[@translate='auth.tfa.promotion.skip']"
navbar="//div[@class='pulsar-header__icon pulsar-header__icon--hamburger ng-isolate-scope']"
purgeCache="//a[@href='/apps/fast-purge/']"
urlradiobutton="//label[@translate='template.ccu.radio.arl']"
textarea="//textarea[@id='arlTextArea']"
submit="//button[@translate='template.ccu.button.submit']"
driver = webdriver.Edge()#Chrome()
time.sleep(4)

def login():
   driver.get(url)
   time.sleep(5)
   driver.find_element_by_xpath(userxpath).send_keys(username)
   time.sleep(5)
   driver.find_element_by_xpath(xpathNext).click()#https://youtu.be/JanCuJSAzhc#find the xpath of a  button in website
   time.sleep(5)
   driver.find_element_by_xpath(passwordxpath).send_keys(password)
   time.sleep(5)
   driver.find_element_by_xpath(signinxpath).click()
   time.sleep(5)
   driver.find_element_by_xpath(skipxpath).click()
   time.sleep(5)
   driver.find_element_by_xpath(navbar).click()
   time.sleep(5)
   driver.find_element_by_xpath(purgeCache).click()
   time.sleep(5)
   driver.find_element_by_xpath(urlradiobutton).click()
   time.sleep(5)
   driver.find_element_by_xpath(textarea).send_keys(url_tobe_cleared)
   time.sleep(5)
   driver.find_element_by_xpath(submit).click()
   time.sleep(5)

login()



'''
Code Utility:Open url in another tab in browser
'''
from selenium import webdriver
import time

driver = webdriver.Edge()#(executable_path=r'TO\Your\Path\geckodriver.exe')
driver.get('https://www.google.com/')

# Open a new window
driver.execute_script("window.open('');")
# Switch to the new window
driver.switch_to.window(driver.window_handles[1])
driver.get("http://stackoverflow.com")
time.sleep(3)

# Open a new window
driver.execute_script("window.open('');")
# Switch to the new window
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.reddit.com/")
time.sleep(3)
# close the active tab
driver.close()
time.sleep(3)

# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])
driver.get("https://bing.com")
time.sleep(3)

# Close the only tab, will also close the browser.
driver.close()
