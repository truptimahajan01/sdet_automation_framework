import logging
from pathlib import Path

_LOG_DIR = Path("reports")


def get_logger(name: str = __name__) -> logging.Logger:
    """Return a configured logger with both console and file handlers.

    Args:
        name: Logger name, typically passed as __name__ from the calling module.

    Returns:
        Configured logging.Logger instance.
    """
    _LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(_LOG_DIR / "framework.log")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

    return logger