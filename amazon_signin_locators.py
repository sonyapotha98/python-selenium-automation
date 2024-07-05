from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=3600&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&language=en_US&pageId=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fmyh%2Fhouseholds%3Flanguage%3Des&prevRID=NGS3D5FSJVAE6MRFQTJM&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Amazon logo
driver.find_element(By.CSS_SELECTOR,'i[aria-label="Amazon"]')

# Create Account
driver.find_element(By.XPATH,'//h1[contains(text(),"Create account")]')

# first name
driver.find_element(By.CSS_SELECTOR,'input#ap_customer_name')

# Email
driver.find_element(By.CSS_SELECTOR,'input#ap_email')

# Password
driver.find_element(By.CSS_SELECTOR,'input#ap_password')

# Passwords must be at least 6 characters.
driver.find_element(By.XPATH,'//div[contains(text(),"Passwords must be at least 6 char")]')

# Re-enter password
driver.find_element(By.CSS_SELECTOR,'input#ap_password_check')

# ID
driver.find_element(By.ID,'continue')

# Conditions of Use
driver.find_element(By.XPATH,'//a[text()="Conditions of Use"]')

# Privacy Notice
driver.find_element(By.XPATH,'//a[text()="Privacy Notice"]')

# Signin
driver.find_element(By.XPATH, "//a[contains(@href,'signin')]")

sleep(5)
