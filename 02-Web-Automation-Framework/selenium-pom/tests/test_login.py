"""
Login Page Tests

This file contains all test cases for the Login functionality.

Test Data:
- Valid username: tomsmith
- Valid password: SuperSecretPassword!
"""

import pytest
from pages.login_page import LoginPage


class TestLogin:
    """
    Test cases for Login functionality
    """
    
    @pytest.mark.smoke
    @pytest.mark.login
    def test_successful_login(self, driver):
        """
        Test Case: Successful login with valid credentials
        
        Steps:
        1. Open login page
        2. Enter valid username
        3. Enter valid password
        4. Click login button
        5. Verify user is logged in
        6. Verify success message is displayed
        """
        # Arrange (Setup)
        login_page = LoginPage(driver)
        login_page.open()
        
        # Act (Perform action)
        login_page.login("tomsmith", "SuperSecretPassword!")
        
        # Assert (Verify result)
        assert login_page.is_logged_in(), "User should be logged in"
        
        success_message = login_page.get_success_message()
        assert "You logged into a secure area!" in success_message, \
            "Success message should be displayed"
    
    
    @pytest.mark.login
    def test_login_with_invalid_username(self, driver):
        """
        Test Case: Login with invalid username
        
        Expected Result: Should show error message
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        # Try to login with invalid username
        login_page.login("invalid_user", "SuperSecretPassword!")
        
        # Verify error message is shown
        error_message = login_page.get_error_message()
        assert "Your username is invalid!" in error_message, \
            "Error message should indicate invalid username"
        
        # Verify user is NOT logged in
        assert not login_page.is_logged_in(), "User should NOT be logged in"
    
    
    @pytest.mark.login
    def test_login_with_invalid_password(self, driver):
        """
        Test Case: Login with invalid password
        
        Expected Result: Should show error message
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        # Try to login with invalid password
        login_page.login("tomsmith", "wrong_password")
        
        # Verify error message is shown
        error_message = login_page.get_error_message()
        assert "Your password is invalid!" in error_message, \
            "Error message should indicate invalid password"
        
        # Verify user is NOT logged in
        assert not login_page.is_logged_in(), "User should NOT be logged in"
    
    
    @pytest.mark.login
    def test_login_with_empty_credentials(self, driver):
        """
        Test Case: Login with empty username and password
        
        Expected Result: Should show error message
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        # Try to login with empty fields
        login_page.login("", "")
        
        # Verify error message is shown
        error_message = login_page.get_error_message()
        assert "Your username is invalid!" in error_message, \
            "Error message should be displayed for empty credentials"
    
    
    @pytest.mark.smoke
    @pytest.mark.login
    def test_logout_functionality(self, driver):
        """
        Test Case: Logout after successful login
        
        Steps:
        1. Login successfully
        2. Click logout button
        3. Verify user is redirected to login page
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        # Login first
        login_page.login("tomsmith", "SuperSecretPassword!")
        assert login_page.is_logged_in(), "User should be logged in"
        
        # Logout
        login_page.logout()
        
        # Verify redirected to login page
        assert "/login" in login_page.get_current_url(), \
            "Should be redirected to login page after logout"
    
    
    @pytest.mark.ui
    def test_login_page_title(self, driver):
        """
        Test Case: Verify login page title
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        page_title = login_page.get_page_title()
        assert "The Internet" in page_title, \
            f"Expected 'The Internet' in title, but got '{page_title}'"
    
    
    @pytest.mark.ui
    def test_login_button_is_visible(self, driver):
        """
        Test Case: Verify login button is visible on page load
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        assert login_page.is_element_visible(login_page.LOGIN_BUTTON), \
            "Login button should be visible"


# Parametrized test example
@pytest.mark.parametrize("username,password,expected_error", [
    ("invalid", "invalid", "Your username is invalid!"),
    ("tomsmith", "wrong", "Your password is invalid!"),
    ("", "", "Your username is invalid!"),
])
def test_login_with_various_invalid_credentials(driver, username, password, expected_error):
    """
    Test Case: Login with various invalid credential combinations
    
    This is a "parametrized test" - it runs multiple times with different data
    Think of it as: 1 test case, multiple test scenarios
    """
    login_page = LoginPage(driver)
    login_page.open()
    
    login_page.login(username, password)
    
    error_message = login_page.get_error_message()
    assert expected_error in error_message, \
        f"Expected error '{expected_error}' but got '{error_message}'"
