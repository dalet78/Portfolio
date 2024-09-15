from playwright.sync_api import Page
from playwright_interface import BrowserActions

class PlaywrightActions(BrowserActions):
    """Concrete implementation of BrowserActions using Playwright with automatic browser handling."""

    def __init__(self, browser_type="chromium", headless=False):
        # Initialize BrowserManager and store browser and page references
        self.manager = BrowserActions()
        self.browser_type = browser_type
        self.headless = headless
        self.page = None

    def _ensure_browser(self):
        """Ensure the browser is open and a page is available."""
        if self.page is None:
            # Open the browser and create a new page if not already opened
            browser = self.manager.open_browser(browser_type=self.browser_type, headless=self.headless)
            self.page = browser.new_page()

    def find_element(self, selector: str):
        """Find an element on the page."""
        self._ensure_browser()
        return self.page.query_selector(selector)

    def press_button(self, selector: str):
        """Click a button on the page."""
        self._ensure_browser()
        element = self.find_element(selector)
        if element:
            element.click()
        else:
            raise Exception(f"Button with selector '{selector}' not found.")

    def write_text(self, selector: str, text: str):
        """Type text into a field."""
        self._ensure_browser()
        element = self.find_element(selector)
        if element:
            element.fill(text)
        else:
            raise Exception(f"Field with selector '{selector}' not found.")

    def write_password(self, selector: str, password: str):
        """Type a password into a field."""
        self.write_text(selector, password)

    def navigate_to(self, url: str):
        """Navigate to a specific URL."""
        self._ensure_browser()
        self.page.goto(url)

    def get_title(self) -> str:
        """Return the title of the current page."""
        self._ensure_browser()
        return self.page.title()
    
    def take_screenshot(self, path: str):
        """Take a screenshot of the current page."""
        self._ensure_browser()
        self.page.screenshot(path=path)

    def wait_for_selector(self, selector: str, timeout: int = 30000):
        """Wait for a specific element to appear on the page."""
        self._ensure_browser()
        self.page.wait_for_selector(selector, timeout=timeout)

    def get_element_text(self, selector: str) -> str:
        """Retrieve the text content of an element."""
        self._ensure_browser()
        element = self.find_element(selector)
        if element:
            return element.inner_text()
        else:
            raise Exception(f"Element with selector '{selector}' not found.")

    def select_dropdown(self, selector: str, value: str):
        """Select an option from a dropdown menu."""
        self._ensure_browser()
        element = self.find_element(selector)
        if element:
            element.select_option(value=value)
        else:
            raise Exception(f"Dropdown with selector '{selector}' not found.")

    def scroll_to_element(self, selector: str):
        """Scroll the page to the element specified by the selector."""
        self._ensure_browser()
        element = self.find_element(selector)
        if element:
            self.page.evaluate("element => element.scrollIntoView()", element)
        else:
            raise Exception(f"Element with selector '{selector}' not found.") 
        
    def select_radio(self, selector: str):
        """Select a radio button."""
        self._ensure_browser()
        element = self.find_element(selector)
        if element:
            if not element.is_checked():
                element.check()
        else:
            raise Exception(f"Radio button with selector '{selector}' not found.")

    def select_checkbox(self, selector: str):
        """Select a checkbox."""
        self._ensure_browser()
        element = self.find_element(selector)
        if element:
            if not element.is_checked():
                element.check()
        else:
            raise Exception(f"Checkbox with selector '{selector}' not found.")

    def verify_radio_checked(self, selector: str) -> bool:
        """Verify if a radio button is checked."""
        self._ensure_browser()
        element = self.find_element(selector)
        if element:
            return element.is_checked()
        else:
            raise Exception(f"Radio button with selector '{selector}' not found.")

    def verify_checkbox_checked(self, selector: str) -> bool:
        """Verify if a checkbox is checked."""
        self._ensure_browser()
        element = self.find_element(selector)
        if element:
            return element.is_checked()
        else:
            raise Exception(f"Checkbox with selector '{selector}' not found.")


if __name__ == "__main__":
    # Initialize PlaywrightActions with Chromium and non-headless mode
    actions = PlaywrightActions(browser_type="chromium", headless=False)

    # Navigate to a website
    actions.navigate_to('https://www.letskodeit.com/practice')

    # Wait for an element to be visible
    actions.wait_for_selector('text="More information"')

    # Take a screenshot of the current page
    actions.take_screenshot('example_page.png')

    # Get the text of a specific element
    text = actions.get_element_text('h1')
    print(f"Page heading: {text}")

    # Select a value from a dropdown menu
    actions.select_dropdown('select[name="dropdown"]', 'value1')

    # Scroll to a specific element
    actions.scroll_to_element('#footer')

    # Close the browser
    actions.manager.close_browser()