import pytest
import os
from playwright.async_api import async_playwright
from Testing_framework.framework.playwright.chrome_browser import PlaywrightActions  

WEB_SITE="https://courses.letskodeit.com/practice"

class TestPlaywrightActions:
    
        
    @pytest.mark.timeout(600)
    @pytest.mark.sanity
    @pytest.mark.asyncio  # Decoratore per test asincroni
    async def test_radio_button_selection(self):
        actions = PlaywrightActions(browser_type="chromium", headless=False)
        await actions.navigate_to(WEB_SITE)  
        await actions.select_radio('#bmwradio')
        assert await actions.verify_radio_checked('#bmwradio'), "BMW radio button should be checked"

    @pytest.mark.timeout(600)
    @pytest.mark.sanity
    @pytest.mark.asyncio  # Decoratore per test asincroni
    async def test_checkbox_selection(self):
        actions = PlaywrightActions(browser_type="chromium", headless=False)
        await actions.navigate_to(WEB_SITE)  
        await actions.select_checkbox('#bmwcheck')
        assert await actions.verify_checkbox_checked('#bmwcheck'), "BMW checkbox should be checked"

    @pytest.mark.timeout(600)
    @pytest.mark.sanity
    @pytest.mark.asyncio  # Decoratore per test asincroni
    async def test_take_screenshot(self):
        actions = PlaywrightActions(browser_type="chromium", headless=False)
        await actions.navigate_to(WEB_SITE)  
        screenshot_path = '/home/dp/MyProject/Portfolio/Testing_framework/screenshot_example.png'
        await actions.take_screenshot(screenshot_path)
        assert os.path.exists(screenshot_path), "Screenshot file should exist"
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)
