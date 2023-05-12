from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://sadikturan.com"

driver.get(url)
time.sleep(2)
driver.maximize_window()

url = "http://github.com/burakyabgu"
driver.get(url)
print(driver.title)

if "burakyabgu" in driver.title:
    driver.save_screenshot("sadikturan-com-homepage.png")
else:
    print("yok")

time.sleep(2)
driver.back()
# driver.forward() # ileri alma
time.sleep(2)
driver.close()