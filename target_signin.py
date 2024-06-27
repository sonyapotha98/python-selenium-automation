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
driver.get('https://www.target.com/')

# searching for a product
driver.find_element(By.XPATH,"//input[@placeholder='What can we help you find?']").send_keys("Novels")
driver.find_element(By.XPATH,"//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)


# selecting SignIn button
driver.find_element(By.XPATH, '//a[@aria-label="Account, sign in"]').click()
sleep(2)
driver.find_element(By.XPATH, '//a[@data-test="accountNav-signIn"]').click()
sleep(2)

# verifying the “Sign into your Target account” text is shown
expected_text = 'Sign into your Target account'
# actual_text = driver.find_element(By.XPATH,'//div[@class="styles__AuthContainerWrapper-sc-19gc5cv-2 jYGMyH"]').text
actual_text = driver.find_element(By.XPATH,'//h1[@class="styles__StyledHeading-sc-1awz1yh-0 styles__AuthHeading-sc-kz6dq2-2 gfuwhI kcHdEa"]').text
print(actual_text)
assert expected_text.upper() in actual_text.upper(), f'{expected_text} != {actual_text}'
print("test passed".upper()+"\n")
sleep(2)

# verifying SignIn button is shown
driver.find_element(By.ID,"login").click()
print("'SignIn' button pressed")
sleep(2)
driver.quit()




