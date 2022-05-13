import logging


MAJOR_VERSION = 0
MINOR_VERSION = 1
BUILD = 'd'  # a: Alpha - b: Beta - rc: Release candidate - d: Debug build


def banner():
    print("              __           ")
    print("  _________ _/ /____  _____")
    print(" / ___/ __ `/ __/ _ \/ ___/")
    print("/ /__/ /_/ / /_/  __/ /    ")
    print("\___/\__,_/\__/\___/_/     ")
    print(f"\ncater interpreter {MAJOR_VERSION}.{MINOR_VERSION}{BUILD}\n")


def setLogLevel(loglvl: str):
    match loglvl.upper():
        case 'INFO':
            logging.basicConfig(
                format='%(levelname)s: %(message)s', level=logging.INFO)
        case 'DEBUG':
            logging.basicConfig(
                format='%(levelname)s: %(message)s', level=logging.DEBUG)
        case 'WARN':
            logging.basicConfig(
                format='%(levelname)s: %(message)s', level=logging.WARNING)
        case 'ERROR':
            logging.basicConfig(
                format='%(levelname)s: %(message)s', level=logging.ERROR)
        case 'CRIT':
            logging.basicConfig(
                format='%(levelname)s: %(message)s', level=logging.CRITICAL)
