from selenium.webdriver.firefox.options import Options


OPTIONS = Options()
OPTIONS.add_argument("--headless")
OPTIONS.add_argument("--width=2560")
OPTIONS.add_argument("--height=1440")

GECKODRIVER_PATH = "/usr/bin/geckodriver"
GECKODRIVER_LOG_PATH = "logs/geckodriver.log"
