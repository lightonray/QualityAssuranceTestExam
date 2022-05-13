import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestFrameDetector(unittest.TestCase):

    """TestFrameDetector
    https://the-internet.herokuapp.com/frames"""
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "https://the-internet.herokuapp.com/frames"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)
        self.assertIn(self.base_url, self.driver.current_url)

    def test_nested_frames(self):
        element = self.driver.find_element(By.LINK_TEXT, "Nested Frames")
        self.assertTrue(element)
        element.click()
        print('Page navigated after click' + self.driver.title)
        time.sleep(5)
        frameleft = self.driver.find_element(By.CSS_SELECTOR, "html > frameset:nth-child(2)")
        self.assertTrue(frameleft)
        time.sleep(2)
        self.driver.save_screenshot("left_frame_detection.png")
       
        def tearDown(self):
            self.driver.close()

if __name__ == '__main__':
    unittest.main()
