import argparse
from pathlib import Path
import logging
from typing import List, Dict, Union


# Todo: colorize levels ?
def set_logging_level(level: str):
    logFormatter = logging.Formatter("%(asctime)s %(levelname)-5.5s  %(message)s", "%y-%m-%d %H:%M:%S")
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    logging.getLogger().addHandler(consoleHandler)
    logging.getLogger().setLevel(level)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description="Script description")
    parser.add_argument("required_param", type=str, help="Required parameter description")
    parser.add_argument("--optional", type=int, default=0, help="Optional parameter description.")
    parser.add_argument('--do_smth', action='store_true', help="Key parameter description.")
    args = parser.parse_args()
    return args


def main():
    set_logging_level("DEBUG")
    args = parse_arguments()


if __name__ == "__main__":
    main()
