from playwright.sync_api import sync_playwright

class BrowserManager:
    _instance = None

    def __new__(cls):
        # Implement Singleton pattern to ensure only one instance of the class is created
        if cls._instance is None:
            cls._instance = super(BrowserManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize Playwright instance
        self.browser = None
        self.playwright = sync_playwright().start()
    
    def open_browser(self, browser_type="chromium", headless=False):
        # Launch the browser if not already open, based on the specified browser type
        if self.browser is None:
            if browser_type == "chromium":
                self.browser = self.playwright.chromium.launch(headless=headless)
            elif browser_type == "firefox":
                self.browser = self.playwright.firefox.launch(headless=headless)
            elif browser_type == "webkit":
                self.browser = self.playwright.webkit.launch(headless=headless)
            else:
                raise ValueError(f"Browser {browser_type} not supported")
        return self.browser

    def close_browser(self):
        # Close the browser and stop Playwright instance
        if self.browser:
            self.browser.close()
            self.browser = None
            self.playwright.stop()

# Utilizzo della classe BrowserManager
# if __name__ == "__main__":
#     manager = BrowserManager()

#     # Aprire un browser Chromium
#     browser = manager.open_browser(browser_type="chromium", headless=False)

#     # Aprire una nuova pagina e navigare
#     page = browser.new_page()
#     page.goto('https://courses.letskodeit.com/practice')
#     print(page.title())

#     # Chiudere il browser
#     manager.close_browser()