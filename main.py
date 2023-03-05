from selenium import webdriver
import time

# driver = webdriver.Edge(executable_path="C:\\Offline\\browserdrivers\\msedgedriver.exe")
# driver = webdriver.Chrome(executable_path="C:\\Offline\\browserdrivers\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\Offline\\browserdrivers\\geckodriver.exe")


driver.get("https://www.google.de")
driver.maximize_window()
print(driver.title)


time.sleep(100)

driver.close()