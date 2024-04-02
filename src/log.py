import logging

class ColoredFormatter(logging.Formatter):
    """A custom formatter to add color to log messages."""

    COLORS = {
        'DEBUG': '\033[94m',  # Blue
        'INFO': '\033[92m',   # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',  # Red
        'CRITICAL': '\033[95m'  # Purple
    }

    RESET = '\033[0m'

    def format(self, record):
        log_level = record.levelname
        log_msg = super().format(record)
        color = self.COLORS.get(log_level, self.RESET)
        return f"{color}{log_msg}{self.RESET}"

def setup_logging():
    """Set up logging configuration."""
    # 刪除預設的 StreamHandler
    root_logger = logging.getLogger()
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    logging.basicConfig(level=logging.INFO,  # 將日誌級別設置為 INFO
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    logger.setLevel(logging.INFO)
