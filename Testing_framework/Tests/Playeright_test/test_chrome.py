import pytest
import os
from playwright.sync_api import sync_playwright
from Testing_framework.framework.playwright.chrome_browser import PlaywrightActions  

WEB_SITE="https://courses.letskodeit.com/practice"

class TestPlaywrightActions:
    @pytest.fixture(scope="class")
    def playwright_setup(self):
        """Setup Playwright environment."""
        with sync_playwright() as p:
            # Initialize PlaywrightActions with Chromium and non-headless mode
            self.actions = PlaywrightActions(browser_type="chromium", headless=False)
            yield self.actions
            # Teardown code to close the browser
            self.actions.manager.close_browser()

    @pytest.mark.timeout(600)
    @pytest.mark.sanity
    def test_radio_button_selection(self, playwright_setup):
        """
        Verify that the BMW radio button can be selected and verified.
        """
        actions = playwright_setup
        actions.navigate_to(WEB_SITE)  # Replace with the actual URL where the HTML is located

        # Interact with the radio button
        actions.select_radio('#bmwradio')

        # Verify the radio button is selected
        assert actions.verify_radio_checked('#bmwradio'), "BMW radio button should be checked"

    @pytest.mark.timeout(600)
    @pytest.mark.sanity
    def test_checkbox_selection(self, playwright_setup):
        """
        Verify that the BMW checkbox can be selected and verified.
        """
        actions = playwright_setup
        actions.navigate_to(WEB_SITE)  # Replace with the actual URL where the HTML is located

        # Interact with the checkbox
        actions.select_checkbox('#bmwcheck')

        # Verify the checkbox is selected
        assert actions.verify_checkbox_checked('#bmwcheck'), "BMW checkbox should be checked"

    @pytest.mark.timeout(600)
    @pytest.mark.sanity
    def test_take_screenshot(self, playwright_setup):
        """
        Verify taking a screenshot of the page.
        """
        actions = playwright_setup
        actions.navigate_to(WEB_SITE)  # Replace with the actual URL where the HTML is located

        # Take a screenshot
        screenshot_path = 'screenshot_example.png'
        actions.take_screenshot(screenshot_path)

        # Verify that the screenshot file exists (this is a simple existence check)
        assert os.path.exists(screenshot_path), "Screenshot file should exist"

        # Optionally, clean up the screenshot file after the test
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)
