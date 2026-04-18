import logging

def get_logger(name="framework_logger"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        file_handler = logging.FileHandler("reports/framework.log")
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            " %(asctime)s | %(levelname)s | %(name)s | %(message)s "
        )

        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

    return logger