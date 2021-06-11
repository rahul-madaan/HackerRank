import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=THE/PATH/TO/YOUR/PROFILE") # change to profile path
chrome_options.add_argument('--profile-directory=Profile 1')

browser = webdriver.Chrome(executable_path="PATH/TO/cromedriver.exe", chrome_options=chrome_options) # change the executable_path too