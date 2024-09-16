import time
import asyncio
from playwright.async_api import Page
from Testing_framework.framework.playwright.playwright_interface import BrowserActions
from Testing_framework.framework.playwright.browser_manager import BrowserManager

class PlaywrightActions(BrowserActions):
    """Concrete implementation of BrowserActions using Playwright with automatic browser handling."""

    def __init__(self, browser_type="chromium", headless=False):
        # Initialize BrowserManager and store browser and page references
        self.manager = BrowserManager()
        self.browser_type = browser_type
        self.headless = headless
        self.page = None 

    async def _ensure_browser(self):
        """Ensure the browser is open and a page is available."""
        if self.page is None:
            # Open the browser and create a new page if not already opened
            browser = await self.manager.open_browser(browser_type=self.browser_type, headless=self.headless)
            self.page = await browser.new_page()

    async def find_element(self, selector: str):
        """Find an element on the page."""
        await self._ensure_browser()
        return await self.page.query_selector(selector)

    async def press_button(self, selector: str):
        """Click a button on the page."""
        await self._ensure_browser()
        element = await self.find_element(selector)
        if element:
            await element.click()
        else:
            raise Exception(f"Button with selector '{selector}' not found.")

    async def write_text(self, selector: str, text: str):
        """Type text into a field."""
        await self._ensure_browser()
        element = await self.find_element(selector)
        if element:
            await element.fill(text)
        else:
            raise Exception(f"Field with selector '{selector}' not found.")

    async def write_password(self, selector: str, password: str):
        """Type a password into a field."""
        await self.write_text(selector, password)

    async def navigate_to(self, url: str):
        """Navigate to a specific URL."""
        await self._ensure_browser()
        await self.page.goto(url)

    async def get_title(self) -> str:
        """Return the title of the current page."""
        await self._ensure_browser()
        return await self.page.title()
    
    async def take_screenshot(self, path: str):
        """Take a screenshot of the current page."""
        await self._ensure_browser()
        await self.page.screenshot(path=path)

    async def wait_for_selector(self, selector: str, timeout: int = 30000):
        """Wait for a specific element to appear on the page."""
        await self._ensure_browser()
        await self.page.wait_for_selector(selector, timeout=timeout)

    async def get_element_text(self, selector: str) -> str:
        """Retrieve the text content of an element."""
        await self._ensure_browser()
        element = await self.find_element(selector)
        if element:
            return await element.inner_text()
        else:
            raise Exception(f"Element with selector '{selector}' not found.")

    async def select_dropdown(self, selector: str, value: str):
        """Select an option from a dropdown menu."""
        await self._ensure_browser()
        element = await self.find_element(selector)
        if element:
            await element.select_option(value=value)
        else:
            raise Exception(f"Dropdown with selector '{selector}' not found.")

    async def scroll_to_element(self, selector: str):
        """Scroll the page to the element specified by the selector."""
        await self._ensure_browser()
        element = await self.find_element(selector)
        if element:
            await self.page.evaluate("element => element.scrollIntoView()", element)
        else:
            raise Exception(f"Element with selector '{selector}' not found.") 
        
    async def select_radio(self, selector: str):
        """Select a radio button."""
        await self._ensure_browser()
        element = await self.find_element(selector)
        if element:
            if not await element.is_checked():
                await element.check()
        else:
            raise Exception(f"Radio button with selector '{selector}' not found.")

    async def select_checkbox(self, selector: str):
        """Select a checkbox."""
        await self._ensure_browser()
        element = await self.find_element(selector)
        if element:
            if not await element.is_checked():
                await element.check()
        else:
            raise Exception(f"Checkbox with selector '{selector}' not found.")

    async def verify_radio_checked(self, selector: str) -> bool:
        """Verify if a radio button is checked."""
        await self._ensure_browser()
        element = await self.find_element(selector)
        if element:
            return await element.is_checked()
        else:
            raise Exception(f"Radio button with selector '{selector}' not found.")

    async def verify_checkbox_checked(self, selector: str) -> bool:
        """Verify if a checkbox is checked."""
        await self._ensure_browser()
        element = await self.find_element(selector)
        if element:
            return await element.is_checked()
        else:
            raise Exception(f"Checkbox with selector '{selector}' not found.")

# async def run_playwright_tests():
#     # Initialize PlaywrightActions with Chromium and non-headless mode
#     actions = PlaywrightActions(browser_type="chromium", headless=False)

#     # Navigate to a website
#     await actions.navigate_to('https://www.letskodeit.com/practice')

#     # Wait for an element to be visible
#     await actions.wait_for_selector('text="More information"')

#     # Take a screenshot of the current page
#     await actions.take_screenshot('example_page.png')

#     # Get the text of a specific element
#     text = await actions.get_element_text('h1')
#     print(f"Page heading: {text}")

#     # Select a value from a dropdown menu
#     await actions.select_dropdown('select[name="dropdown"]', 'value1')

#     # Scroll to a specific element
#     await actions.scroll_to_element('#footer')

#     # Close the browser
#     actions.manager.close_browser()

# if __name__ == "__main__":
#     asyncio.run(run_playwright_tests())