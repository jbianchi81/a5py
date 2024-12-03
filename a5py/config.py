import configparser
import os

config_path = os.path.join(os.environ["HOME"],".a5py.ini")

def read_config(file_path : str = config_path) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(file_path)

    # # Access sections and options
    # for section in config.sections():
    #     print(f"Section: {section}")
    #     for option in config.options(section):
    #         value = config.get(section, option)
    #         print(f"  {option} = {value}")

    return config

config = read_config()
