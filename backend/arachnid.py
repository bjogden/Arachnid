from __future__ import annotations
import time
from typing import Union
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from config import (
    OPTIONS,
    GECKODRIVER_LOG_PATH,
    GECKODRIVER_PATH,
)


class Arachnid:
    """Initialize Arachnid instance that wraps Selenium Firefox."""

    INSTANCE = None

    def __init__(
        self,
        page_load_wait_duration: int = 3,
        driver_path: str = GECKODRIVER_PATH,
        driver_log_path: str = GECKODRIVER_LOG_PATH,
        driver_options: Options = OPTIONS,
    ) -> None:
        if not self.INSTANCE:
            self._service = Service(
                executable_path=driver_path,
                log_path=driver_log_path,
            )

            self.INSTANCE = Firefox(
                options=driver_options,
                service=self._service,
            )

        self.page_load_wait_duration = page_load_wait_duration

    def get(self, url: str) -> Union[Firefox, None]:
        if not self.INSTANCE:
            raise Exception("You must initialize an Arachnid instance.")

        try:
            self.INSTANCE.get(url)

            if self.page_load_wait_duration:
                print(f"Loaded. Waiting {self.page_load_wait_duration} seconds...")
                # Explicit wait for page load
                time.sleep(self.page_load_wait_duration)

            return self.INSTANCE

        except Exception as e:
            print(f"Driver `get` error {e}")

            self.INSTANCE.quit()

    def execute_js(self, js: str):
        return self.INSTANCE.execute_script(js)

    def get_screenshot(self, fname: str):
        if not fname.endswith(".png"):
            fname += ".png"

        return self.INSTANCE.save_screenshot(fname)

    def quit(self):
        if not self.INSTANCE:
            return

        self.INSTANCE.close()
        self.INSTANCE.quit()
        self._service.stop()
        self.INSTANCE = None
