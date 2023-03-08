from selenium import webdriver
import time

browser = "edge"

# ============================== Standard/Old Variant ======================================
# driver = webdriver.Edge(executable_path="C:\\Offline\\browserdrivers\\msedgedriver.exe")
# driver = webdriver.Chrome(executable_path="C:\\Offline\\browserdrivers\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\\Offline\\browserdrivers\\geckodriver.exe")

# =============== Better Variant (Package: pip install webdriver-manager) ==================
if (browser == "chrome"):
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

if (browser == "firefox"):
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from webdriver_manager.firefox import GeckoDriverManager
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

if (browser == "edge"):
    from selenium.webdriver.edge.service import Service as EdgeService
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("https://www.google.de")
driver.maximize_window()
print(driver.title)


time.sleep(5)

driver.close()
