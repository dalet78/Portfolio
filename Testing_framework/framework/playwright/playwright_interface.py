from abc import ABC, abstractmethod

class BrowserActions(ABC):
    """Abstract base class defining the browser actions interface."""
    
    # Existing methods
    @abstractmethod
    def find_element(self, selector: str):
        pass

    @abstractmethod
    def press_button(self, selector: str):
        pass

    @abstractmethod
    def write_text(self, selector: str, text: str):
        pass

    @abstractmethod
    def write_password(self, selector: str, password: str):
        pass

    @abstractmethod
    def navigate_to(self, url: str):
        pass

    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def take_screenshot(self, path: str):
        """Take a screenshot of the current page."""
        pass

    @abstractmethod
    def wait_for_selector(self, selector: str, timeout: int = 30000):
        """Wait for a specific element to appear on the page."""
        pass

    @abstractmethod
    def get_element_text(self, selector: str) -> str:
        """Retrieve the text content of an element."""
        pass

    @abstractmethod
    def select_dropdown(self, selector: str, value: str):
        """Select an option from a dropdown menu."""
        pass

    @abstractmethod
    def scroll_to_element(self, selector: str):
        """Scroll the page to the element specified by the selector."""
        pass

    @abstractmethod
    def select_radio(self, selector: str):
        """Select a radio button."""
        pass

    @abstractmethod
    def select_checkbox(self, selector: str):
        """Select a checkbox."""
        pass

    @abstractmethod
    def verify_radio_checked(self, selector: str) -> bool:
        """Verify if a radio button is checked."""
        pass

    @abstractmethod
    def verify_checkbox_checked(self, selector: str) -> bool:
        """Verify if a checkbox is checked."""
        pass
