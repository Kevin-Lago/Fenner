import logging
from src.lucid_loading_bar import LucidLoadingBar
from src import lucid_logging_formaters
from src import lucid_logging_handlers

if not hasattr(logging, 'loading_bar'):
    setattr(logging, 'loading_bar', LucidLoadingBar())

DEBUG = True
COLORED_LOGS = True
lucid_rotating_file_handler = lucid_logging_handlers.LucidTimedRotatingFileHandler(
    directory='./logs/',
    when='midnight',
    interval=1,
    file_extension='log'
)
lucid_rotating_file_handler.setFormatter(lucid_logging_formaters.LucidFileFormatter())
lucid_stream_handler = lucid_logging_handlers.LucidStreamHandler()
lucid_stream_handler.setFormatter(lucid_logging_formaters.LucidStreamFormatter())
logging.basicConfig(
    level=10 if DEBUG else 15,
    handlers=[lucid_stream_handler, lucid_rotating_file_handler]
)

logger = logging.getLogger("Mercury")

logger.critical("Critical Test")
logger.error("Error Test")
logger.warning("Warning Test")
logger.info("Info Test")
# logger.init("Init Test")
logger.debug("Debug Test")


def add_logging_level(level_name, level_num, method_name=None):
    if not method_name:
        method_name = level_name.lower()

    if hasattr(logging, level_name):
        raise AttributeError('Level "{}" already defined in logging module'.format(level_name))
    if hasattr(logging, method_name):
        raise AttributeError('Method "{}" already defined in logging module'.format(method_name))
    if hasattr(logging.getLoggerClass(), method_name):
        raise AttributeError('Method "{}" already defined in logging class'.format(method_name))

    def log_for_level(self, message, *args, **kwargs):
        if self.isEnabledFor(level_num):
            self._log(level_num, message, args, **kwargs)

    def log_to_root(message, *args, **kwargs):
        logging.log(level_num, message, *args, **kwargs)

    logging.addLevelName(level_num, level_name)
    setattr(logging, level_name, level_num)
    setattr(logging.getLoggerClass(), method_name, log_for_level)
    setattr(logging, method_name, log_to_root)


