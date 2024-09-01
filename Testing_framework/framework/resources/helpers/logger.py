import logging

DEFAULT_LOG_FILENAME = 'test.log'  # Improved naming for clarity


class LoggerClass:
    """
    Improved Logger class with enhanced features and error handling.
    """

    def __init__(self, file_log_path=DEFAULT_LOG_FILENAME):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        try:
            self.set_log_path(file_log_path)
        except (IOError, OSError) as e:  # Handle potential file-related errors
            print(f"Error setting log path: {e}")
            self.logger.error(f"Error setting log path: {e}")  # Log the error

    def set_log_path(self, file_log_path):
        # Clear existing handlers (same approach as previous responses)
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        # Create a new handler with improved formatting and error handling
        try:
            file_handler = logging.FileHandler(file_log_path)
            file_handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler) 

        except (IOError, OSError) as e:
            print(f"Error creating file handler: {e}")
            self.logger.error(f"Error creating file handler: {e}")  # Log the error

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message): 
        self.logger.critical(message) 
