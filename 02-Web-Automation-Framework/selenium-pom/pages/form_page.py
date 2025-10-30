"""
Form Page Object

This class represents a form page with various input types.

URL: https://the-internet.herokuapp.com/dropdown
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class FormPage(BasePage):
    """
    Page Object for Form/Dropdown Page
    """
    
    # Page URL
    URL = "https://the-internet.herokuapp.com/dropdown"
    
    # Locators
    DROPDOWN = (By.ID, "dropdown")
    
    
    def __init__(self, driver):
        """
        Initialize Form Page
        
        Args:
            driver: Selenium WebDriver instance
        """
        super().__init__(driver)
    
    
    def open(self):
        """
        Open the form page
        """
        self.open_url(self.URL)
    
    
    def select_dropdown_by_value(self, value):
        """
        Select dropdown option by value
        
        Args:
            value: Value to select (e.g., "1", "2")
        """
        dropdown_element = self.find_element(self.DROPDOWN)
        select = Select(dropdown_element)
        select.select_by_value(value)
    
    
    def select_dropdown_by_text(self, text):
        """
        Select dropdown option by visible text
        
        Args:
            text: Text to select (e.g., "Option 1")
        """
        dropdown_element = self.find_element(self.DROPDOWN)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)
    
    
    def get_selected_option_text(self):
        """
        Get the currently selected option text
        
        Returns:
            Selected option text
        """
        dropdown_element = self.find_element(self.DROPDOWN)
        select = Select(dropdown_element)
        return select.first_selected_option.text
