"""
Form Tests

This file contains test cases for form interactions (dropdowns, inputs, etc.)
"""

import pytest
from pages.form_page import FormPage


class TestForm:
    """
    Test cases for Form functionality
    """
    
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_select_dropdown_option_1(self, driver):
        """
        Test Case: Select Option 1 from dropdown
        
        Steps:
        1. Open dropdown page
        2. Select "Option 1"
        3. Verify option is selected
        """
        form_page = FormPage(driver)
        form_page.open()
        
        # Select option by text
        form_page.select_dropdown_by_text("Option 1")
        
        # Verify selection
        selected_text = form_page.get_selected_option_text()
        assert selected_text == "Option 1", \
            f"Expected 'Option 1' but got '{selected_text}'"
    
    
    @pytest.mark.ui
    def test_select_dropdown_option_2(self, driver):
        """
        Test Case: Select Option 2 from dropdown
        """
        form_page = FormPage(driver)
        form_page.open()
        
        # Select option by value
        form_page.select_dropdown_by_value("2")
        
        # Verify selection
        selected_text = form_page.get_selected_option_text()
        assert selected_text == "Option 2", \
            f"Expected 'Option 2' but got '{selected_text}'"
    
    
    @pytest.mark.ui
    def test_dropdown_page_title(self, driver):
        """
        Test Case: Verify dropdown page title
        """
        form_page = FormPage(driver)
        form_page.open()
        
        page_title = form_page.get_page_title()
        assert "The Internet" in page_title


@pytest.mark.parametrize("option_value,option_text", [
    ("1", "Option 1"),
    ("2", "Option 2"),
])
def test_select_dropdown_options_parametrized(driver, option_value, option_text):
    """
    Test Case: Select different dropdown options (parametrized)
    
    This test runs twice:
    - Once with Option 1
    - Once with Option 2
    """
    form_page = FormPage(driver)
    form_page.open()
    
    form_page.select_dropdown_by_value(option_value)
    
    selected_text = form_page.get_selected_option_text()
    assert selected_text == option_text
