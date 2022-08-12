from selenium.webdriver.firefox.options import Options


OPTIONS = Options()
OPTIONS.add_argument("--headless")

GECKODRIVER_PATH = '/usr/bin/geckodriver'
GECKODRIVER_LOG_PATH = 'logs/geckodriver.log'
