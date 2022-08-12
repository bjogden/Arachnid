from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


options = Options()
options.add_argument("--headless")

service = Service(
    executable_path='/usr/bin/geckodriver',
    log_path='logs/geckodriver.log',
)
