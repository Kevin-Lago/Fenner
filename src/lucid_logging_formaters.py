import logging


class LucidStreamFormatter(logging.Formatter):
    grey = "\033[38;2;200;200;200m"
    white = "\033[38;2;255;255;255m"
    red = "\033[38;2;255;0;0m"
    yellow = "\033[38;2;255;255;0m"
    green = "\033[38;2;0;150;0m"
    lime = "\033[38;2;0;255;0m"
    cyan = "\033[38;2;0;255;255m"
    blue = "\033[38;2;0;0;255m"
    purple = "\033[38;2;0;0;150m"
    format = "[%(asctime)s][$COLOR%(levelname)s$RESET]$FILE$LINE %(message)s$RESET"

    FORMATS = {
        logging.CRITICAL: grey + format.replace("$COLOR", green if True else '').replace("$RESET", grey)
        .replace("$FILE", "[%(filename)s:").replace("$LINE", "%(lineno)d]"),

        logging.ERROR: grey + format.replace("$COLOR", lime if True else '').replace("$RESET", grey)
        .replace("$FILE", "[%(filename)s:").replace("$LINE", "%(lineno)d]"),

        logging.WARNING: grey + format.replace("$COLOR", blue if True else '').replace("$RESET", grey)
        .replace("$FILE", "[%(filename)s:").replace("$LINE", "%(lineno)d]"),

        logging.INFO: grey + format.replace("$COLOR", purple if True else '').replace("$RESET", grey)
        .replace("$FILE", "").replace("$LINE", ""),

        logging.DEBUG: grey + format.replace("$COLOR", lime if True else '').replace("$RESET", grey)
        .replace("$FILE", "").replace("$LINE", ""),
    }

    def add_level_format(self, level_no, format=None):
        self.FORMATS[level_no] = format if format else self.format

    def __init__(self, format=None, datefmt=None):
        # self.format = format if format else "[%(asctime)s][$COLOR%(levelname)s$RESET]$FILE$LINE %(message)s"
        self.datefmt = datefmt if datefmt else "%m/%d/%Y %H:%M:%S"

    def format(self, record):
        log_format = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format)
        formatter.datefmt = self.datefmt
        return formatter.format(record=record)


class LucidFileFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno in [logging.CRITICAL, logging.ERROR, logging.WARNING]:
            return logging.Formatter("[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)d] %(message)s").format(record)
        return logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s").format(record)
