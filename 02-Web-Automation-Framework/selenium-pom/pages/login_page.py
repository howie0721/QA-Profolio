"""
Login Page Object

This class represents the Login page on the website.
It inherits from BasePage and adds login-specific methods.

URL: https://the-internet.herokuapp.com/login
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for Login Page
    """
    
    # Page URL
    URL = "https://the-internet.herokuapp.com/login"
    
    # Locators (Element identifiers)
    # Format: (By.METHOD, "value")
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#flash")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#flash.error")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    
    
    def __init__(self, driver):
        """
        Initialize Login Page
        
        Args:
            driver: Selenium WebDriver instance
        """
        super().__init__(driver)
    
    
    def open(self):
        """
        Open the login page
        """
        self.open_url(self.URL)
    
    
    def enter_username(self, username):
        """
        Enter username in the username field
        
        Args:
            username: Username string
        """
        self.type_text(self.USERNAME_INPUT, username)
    
    
    def enter_password(self, password):
        """
        Enter password in the password field
        
        Args:
            password: Password string
        """
        self.type_text(self.PASSWORD_INPUT, password)
    
    
    def click_login_button(self):
        """
        Click the login button
        """
        self.click(self.LOGIN_BUTTON)
    
    
    def login(self, username, password):
        """
        Complete login process
        This is a "helper method" that combines all steps
        
        Args:
            username: Username string
            password: Password string
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    
    def get_success_message(self):
        """
        Get the success message after login
        
        Returns:
            Success message text
        """
        return self.get_text(self.SUCCESS_MESSAGE)
    
    
    def get_error_message(self):
        """
        Get the error message after failed login
        
        Returns:
            Error message text
        """
        return self.get_text(self.ERROR_MESSAGE)
    
    
    def is_logged_in(self):
        """
        Check if user is logged in
        (by checking if logout button is visible)
        
        Returns:
            True if logged in, False otherwise
        """
        return self.is_element_visible(self.LOGOUT_BUTTON)
    
    
    def logout(self):
        """
        Click the logout button
        """
        self.click(self.LOGOUT_BUTTON)
