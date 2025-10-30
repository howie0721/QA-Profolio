"""
Base Page - Parent class for all page objects

This is like a "template" that all other pages will inherit from.
It contains common methods that every page needs (click, type, wait, etc.)

Think of it as the "basic tools" that all pages can use.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BasePage:
    """
    Base class for all page objects
    All page classes should inherit from this
    """
    
    def __init__(self, driver):
        """
        Initialize the page with a driver
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    
    
    def open_url(self, url):
        """
        Open a URL in the browser
        
        Args:
            url: Website URL to open
        """
        self.driver.get(url)
    
    
    def find_element(self, locator):
        """
        Find a single element on the page
        
        Args:
            locator: Tuple of (By.method, "value")
            Example: (By.ID, "username")
            
        Returns:
            WebElement object
        """
        return self.wait.until(EC.presence_of_element_located(locator))
    
    
    def find_elements(self, locator):
        """
        Find multiple elements on the page
        
        Args:
            locator: Tuple of (By.method, "value")
            
        Returns:
            List of WebElement objects
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    
    def click(self, locator):
        """
        Click on an element
        
        Args:
            locator: Tuple of (By.method, "value")
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    
    def type_text(self, locator, text):
        """
        Type text into an input field
        
        Args:
            locator: Tuple of (By.method, "value")
            text: Text to type
        """
        element = self.find_element(locator)
        element.clear()  # Clear existing text first
        element.send_keys(text)
    
    
    def get_text(self, locator):
        """
        Get text from an element
        
        Args:
            locator: Tuple of (By.method, "value")
            
        Returns:
            Text content of the element
        """
        element = self.find_element(locator)
        return element.text
    
    
    def is_element_visible(self, locator, timeout=10):
        """
        Check if an element is visible on the page
        
        Args:
            locator: Tuple of (By.method, "value")
            timeout: Maximum time to wait (seconds)
            
        Returns:
            True if element is visible, False otherwise
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    
    def get_page_title(self):
        """
        Get the current page title
        
        Returns:
            Page title as string
        """
        return self.driver.title
    
    
    def get_current_url(self):
        """
        Get the current page URL
        
        Returns:
            Current URL as string
        """
        return self.driver.current_url
    
    
    def take_screenshot(self, filename):
        """
        Take a screenshot of the current page
        
        Args:
            filename: Path to save the screenshot
        """
        self.driver.save_screenshot(filename)
