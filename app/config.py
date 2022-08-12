from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


OPTIONS = Options()
OPTIONS.add_argument("--headless")

SERVICE = Service(
    executable_path='/usr/bin/geckodriver',
    log_path='logs/geckodriver.log',
)
