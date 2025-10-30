"""
pytest configuration file for Web Automation tests

This file provides fixtures (reusable setup code) for tests.
"""

import pytest
from utils.driver_factory import DriverFactory


def pytest_addoption(parser):
    """
    Add command line options to pytest
    
    Usage:
        pytest --browser=chrome
        pytest --browser=firefox --headless
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests (chrome, firefox, edge)"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode (no UI)"
    )


@pytest.fixture(scope="function")
def driver(request):
    """
    Create and provide a browser driver for each test
    
    This fixture:
    1. Creates a browser driver before each test
    2. Provides it to the test
    3. Closes it after the test finishes
    
    Usage in tests:
        def test_something(driver):
            driver.get("https://example.com")
    """
    # Get command line options
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    
    # Create driver
    driver = DriverFactory.get_driver(browser, headless)
    
    # Provide driver to test
    yield driver
    
    # Cleanup: close browser after test
    driver.quit()


@pytest.fixture(scope="function")
def driver_with_screenshot(request, driver):
    """
    Driver fixture that takes screenshot on test failure
    
    Usage in tests:
        def test_something(driver_with_screenshot):
            # test code
    """
    yield driver
    
    # Take screenshot if test failed
    if request.node.rep_call.failed:
        screenshot_name = f"screenshot_{request.node.name}.png"
        driver.save_screenshot(screenshot_name)
        print(f"\nScreenshot saved: {screenshot_name}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test result for screenshot fixture
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
