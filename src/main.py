import logging
from src import __init__
from time import sleep

logger = logging.getLogger("test")

def colored(x, y, r, g, b, text):
    return "\033[1;0;2m\033[{};{};{};{};{}m{}\033[1;0;2m".format(x, y, r, g, b, text)


text = 'Hello, World'

for j in range(256):
    print(f"\033[{j};2m\033[{38};{2};{255};{255};{j}m{text}\033[38;2;255;255;255m")


def main():
    print()
    # test = [1,2,2,2,2,2,2]
    # # loading_bar.init_loading_bar(test, "test")
    # logger.loading_bar.init_loading_bar(test, "test")
    #
    # for int in test:
    #     logger.log(int)
    #     sleep(2)


if __name__ == '__main__':
    main()
