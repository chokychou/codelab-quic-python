import logging
import sys
from src.http.core.config import settings

def configure_logging():
    """Configures the logging system for the application."""

    # Get the root logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG if settings.is_development else logging.INFO)

    # Create a formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Create a stream handler (for console output)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # Create a file handler (for file output)
    # if settings.is_production:
    #     file_handler = logging.FileHandler("app.log")
    #     file_handler.setFormatter(formatter)
    #     logger.addHandler(file_handler)

    # Example of creating a specific logger
    # api_logger = logging.getLogger("api")
    # api_logger.setLevel(logging.DEBUG)
    # api_logger.addHandler(stream_handler)
    # api_logger.addHandler(file_handler)

    return
