import sys
import logging


class LucidStreamFormatter(logging.Formatter):
    reset = "\033[38;2;200;200;200m" if not sys.stdout.isatty() else ''
    red = "\033[91m"
    yellow = "\033[93m"
    green = "\033[92m"
    # lime = "\033[38;2;0;255;0m"
    cyan = "\033[96m"
    blue = "\033[94m"
    # purple = "\033[38;2;0;0;150m"
    magenta = "\033[95"
    format = "[%(asctime)s][$COLOR%(levelname)s$RESET]$FILE$LINE %(message)s$RESET"

    FORMATS = {
        logging.CRITICAL: reset + format.replace("$COLOR", red if True else '').replace("$RESET", reset)
        .replace("$FILE", "[%(filename)s:").replace("$LINE", "%(lineno)d]"),

        logging.ERROR: reset + format.replace("$COLOR", red if True else '').replace("$RESET", reset)
        .replace("$FILE", "[%(filename)s:").replace("$LINE", "%(lineno)d]"),

        logging.WARNING: reset + format.replace("$COLOR", yellow if True else '').replace("$RESET", reset)
        .replace("$FILE", "[%(filename)s:").replace("$LINE", "%(lineno)d]"),

        logging.INFO: reset + format.replace("$COLOR", cyan if True else '').replace("$RESET", reset)
        .replace("$FILE", "").replace("$LINE", ""),

        logging.DEBUG: reset + format.replace("$COLOR", magenta if True else '').replace("$RESET", reset)
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
