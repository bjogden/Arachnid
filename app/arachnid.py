import time
from selenium.webdriver import Firefox
from typing import Union
from __future__ import annotations

from config import OPTIONS, SERVICE


class Arachnid:
    """Initialize Arachnid instance that wraps Selenium Firefox."""
    INSTANCE = None
    
    def __init__(self) -> Union[Arachnid, None]:
        if self.INSTANCE:
            return self.INSTANCE
        
        self.INSTANCE = Firefox(
            options=OPTIONS,
            service=SERVICE,
        )
        
    def get(self, url: str) -> Union[Firefox, None]:
        if not self.INSTANCE:
            raise Exception('You must initialize an Arachnid instance.')
        
        try:
            self.INSTANCE.get(url)
            # Explicit wait for page load
            time.sleep(3)
            
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
