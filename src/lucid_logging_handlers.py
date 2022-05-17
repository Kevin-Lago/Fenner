import logging
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler


class LucidTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, directory, when, interval, file_extension):
        self.directory = directory
        self.when = when
        self.interval = interval
        self.file_extension = file_extension
        filename = f"{self.directory}{self.generateFileName()}.{self.file_extension}"
        TimedRotatingFileHandler.__init__(self, filename=filename, when=when, interval=interval)

    def doRollover(self):
        self.stream.close()
        self.baseFilename = f"{self.directory}{self.generateFileName()}.{self.file_extension}"
        self.stream = open(self.baseFilename, 'a')
        self.rolloverAt = self.rolloverAt + self.interval

    def generateFileName(self):
        date_format = ""
        return datetime.now().strftime(date_format)


class LucidStreamHandler(logging.StreamHandler):
    def __init__(self):
        logging.StreamHandler.__init__(self)

    def emit(self, record):
        message = self.format(record)
        stream = self.stream
        stream.write(message + self.terminator)
        if logging.loading_bar.is_loading:
            stream.write(logging.loading_bar.get_loading_bar())
            logging.loading_bar.progress_loading_bar()
        self.flush()
