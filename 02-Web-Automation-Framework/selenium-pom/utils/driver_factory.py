"""
Driver Factory - Browser Driver Management

This file creates and manages browser drivers (Chrome, Firefox, Edge)
Think of this as a "browser factory" - you tell it which browser you want,
and it gives you a ready-to-use browser driver.

Note: Selenium 4.6+ includes automatic driver management, so we don't need webdriver-manager
"""

from selenium import webdriver


class DriverFactory:
    """
    Factory class to create browser drivers
    """
    
    @staticmethod
    def get_driver(browser_name="chrome", headless=False):
        """
        Create and return a browser driver
        
        Args:
            browser_name: Name of browser (chrome, firefox, edge)
            headless: Run browser in background without UI (True/False)
            
        Returns:
            WebDriver object
        """
        
        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            # Add useful options
            options.add_argument("--start-maximized")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            # Selenium 4.6+ automatically manages ChromeDriver
            driver = webdriver.Chrome(options=options)
            
        elif browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            
            if headless:
                options.add_argument("--headless")
                
            driver = webdriver.Firefox(options=options)
            
        elif browser_name.lower() == "edge":
            options = webdriver.EdgeOptions()
            
            if headless:
                options.add_argument("--headless=new")
                
            driver = webdriver.Edge(options=options)
            
        else:
            raise ValueError(f"Browser '{browser_name}' is not supported")
        
        # Set implicit wait (wait up to 10 seconds for elements to appear)
        driver.implicitly_wait(10)
        
        return driver
