import time
from selenium.webdriver import Firefox
from typing import Union

from config import OPTIONS, SERVICE


class Arachnid:
    def __init__(self) -> None:       
        self._DRIVER = None
        
    @classmethod
    def get(cls, url: str) -> Union[Firefox, None]:
        obj = cls()
        
        try:
            obj.DRIVER.get(url)
            # Explicit wait for page load
            time.sleep(3)
            
            return obj

        except Exception as e:
            print(f'Driver `get` error {e}')
            
            cls.DRIVER.quit()
        
    def execute_js(self, js: str):
        return self.DRIVER.execute_script(js)
    
    def get_screenshot(self, fname: str):
        if not fname.endswith('.png'):
            fname += '.png'
            
        return self.DRIVER.save_screenshot(fname)
    
    def quit(self):
        self.DRIVER.quit()
        self.DRIVER = None
        
    @property
    def DRIVER(self):
        if not self._DRIVER:
            self._DRIVER = Firefox(
                options=OPTIONS,
                service=SERVICE,
            )
        
        return self._DRIVER
