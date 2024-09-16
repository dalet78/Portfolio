from playwright.async_api import async_playwright

class BrowserManager:
    _instance = None

    def __new__(cls):
        # Implement Singleton pattern to ensure only one instance of the class is created
        if cls._instance is None:
            cls._instance = super(BrowserManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize Playwright instance (deferred to `open_browser`)
        self.browser = None
        self.playwright = None

    async def open_browser(self, browser_type="chromium", headless=False):
        # Start Playwright and launch the browser if not already open
        if self.browser is None:
            self.playwright = await async_playwright().start()

            if browser_type == "chromium":
                self.browser = await self.playwright.chromium.launch(headless=headless)
            elif browser_type == "firefox":
                self.browser = await self.playwright.firefox.launch(headless=headless)
            elif browser_type == "webkit":
                self.browser = await self.playwright.webkit.launch(headless=headless)
            else:
                raise ValueError(f"Browser {browser_type} not supported")
        return self.browser

    async def close_browser(self):
        # Close the browser and stop Playwright instance
        if self.browser:
            await self.browser.close()
            self.browser = None

        if self.playwright:
            await self.playwright.stop()
            self.playwright = None
