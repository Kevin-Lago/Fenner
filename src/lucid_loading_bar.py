class LucidLoadingBar:
    def __init__(self, iterable=None, prefix='', suffix='', decimals=1, length=100, fill='\u2588', print_end='\r', is_loading=None):
        self.iterable = iterable
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.print_end = print_end
        self.is_loading = is_loading
        self.progress = 0
        self.total = 0

    def get_loading_bar(self):
        percent = ("{0:." + str(self.decimals) + "f}").format(100 * (self.progress / float(self.total)))
        filled_length = int(self.length * self.progress // self.total)
        bar = self.fill * filled_length + "-" * (self.length - filled_length)
        return f'\r{self.prefix} |{bar}| {percent}%% {self.suffix}\r'

    def init_loading_bar(self, iterable, prefix):
        self.is_loading = True
        self.total = len(iterable)
        self.prefix = prefix
        return self

    def finish_loading(self):
        self.is_loading = False
        self.total = 0
        self.prefix = ''
        self.progress = 0

    def progress_loading_bar(self):
        self.progress += 1
