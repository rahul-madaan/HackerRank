import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--user-data-dir=chrome-data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome("E:\\Downloads\\chromedriver2.exe", options=options)

driver.get('https://web.whatsapp.com')

time.sleep(25)

driver.find_element_by_xpath("//*[@title='Full lamebaazi by adt']").click()

message = ""
for i in range(29):
    message = message + "."
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
    time.sleep(1)


