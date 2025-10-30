"""
Driver Factory - Browser Driver Management

This file creates and manages browser drivers (Chrome, Firefox, Edge)
Think of this as a "browser factory" - you tell it which browser you want,
and it gives you a ready-to-use browser driver.

Note: Selenium 4.6+ includes automatic driver management, so we don't need webdriver-manager
"""

import os
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
        # 在 CI 或設有 HEADLESS 環境變數時強制使用 headless
        env_headless = str(os.environ.get("HEADLESS", "")).lower() in {"1", "true", "yes"}
        ci_env = str(os.environ.get("CI", "")).lower() in {"1", "true", "yes"}
        effective_headless = headless or env_headless or ci_env

        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            if effective_headless:
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
                # 避免 Headless 新模式的除錯埠衝突
                options.add_argument("--remote-debugging-port=0")
            else:
                options.add_argument("--start-maximized")
            # Add useful options
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-first-run")
            options.add_argument("--no-default-browser-check")
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
