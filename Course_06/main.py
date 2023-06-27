from logger_36 import LOGGER
import requests


def print_hi(name):
    print(f'Hi, {name}')
    response = requests.get("https://google.com")
    print(response.status_code)
    LOGGER.warning("Function ended")


if __name__ == '__main__':
    print_hi('PyCharm')
