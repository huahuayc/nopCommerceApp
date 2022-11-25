from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#serv_obj = Service("C:\BrowserDrivers\chromedriver.exe")
serv_obj = Service()
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Edge(service=serv_obj)

url ="https://demo.guru99.com/v4/"  # "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"  #
driver.get(url)



print("a simple test")