import time
from selenium.webdriver import Firefox
from typing import Union
from __future__ import annotations

from config import OPTIONS, SERVICE


class Arachnid:
    """Initialize Arachnid instance that wraps Selenium Firefox."""
    INSTANCE = None
    
    def __init__(self, page_load_wait_duration: int = 3) -> None:
        if not self.INSTANCE:
            self.INSTANCE = Firefox(
                options=OPTIONS,
                service=SERVICE,
            )

        self.page_load_wait_duration = page_load_wait_duration
        
    def get(self, url: str) -> Union[Firefox, None]:
        if not self.INSTANCE:
            raise Exception('You must initialize an Arachnid instance.')
        
        try:
            self.INSTANCE.get(url)

            if self.page_load_wait_duration:
                print(f'Loaded. Waiting {self.page_load_wait_duration} seconds...')
                # Explicit wait for page load
                time.sleep(self.page_load_wait_duration)
            
            return self.INSTANCE

        except Exception as e:
            print(f'Driver `get` error {e}')
            
            self.INSTANCE.quit()
        
    def execute_js(self, js: str):
        return self.INSTANCE.execute_script(js)
    
    def get_screenshot(self, fname: str):
        if not fname.endswith('.png'):
            fname += '.png'
            
        return self.INSTANCE.save_screenshot(fname)
    
    def quit(self):
        if not self.INSTANCE:
            return
        
        self.INSTANCE.quit()
        self.INSTANCE = None
