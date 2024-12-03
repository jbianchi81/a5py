import configparser
import os
from setuptools import setup, find_packages
from setuptools.command.install import install

# config path
config_path = os.path.join(os.environ["HOME"],".a5py.ini")

def create_ini_from_dict(config_dict, config_path = config_path):
    """
    Create an .ini configuration file from a dictionary.
    
    :param config_dict: Dictionary containing configuration data.
                        Format: {section: {key: value, ...}, ...}
    :param file_path: Path to the .ini file to be created.
    """
    config = configparser.ConfigParser()
    
    # Populate ConfigParser with sections and keys
    for section, options in config_dict.items():
        config[section] = options
    
    # Write the configuration to a file
    if os.path.exists(config_path):
        user_input = input("Configuration file already exists. Overwrite? y/n:").strip().lower()
        if user_input in ['y', 'yes']:
            with open(config_path, 'w') as configfile:
                config.write(configfile)
            print("Configuration file '%s' created successfully. Edit the file to modify the default configuration" % config_path)
        else:
            print("Configuration file not written")

# Default config
config_data = {
    "db_params": {
        "dbname": "a5",
        "username": "username",
        "password": "password",
        "host": "localhost",
        "port": 5432
    },
    "test_db_params": {
        "dbname": "a5_test",
        "username": "username",
        "password": "password",
        "host": "localhost",
        "port": 5432
    },
    "raster": {
        "path": os.path.join(os.environ["HOME"],"a5/data/raster"),
        "bbox.ulx": -70, 
        "bbox.uly": -10,
        "bbox.lrx":-40, 
        "bbox.lry": -40
    }
}

class CustomInstallCommand(install):
    def run(self):
        create_ini_from_dict(config_data, config_path)
        super().run()

setup(
    name="a5py",
    version="1.0",
    packages=find_packages(),
    description='a5 hydrometeorologic database management system',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='Juan F. Bianchi',
    author_email='jbianchi@ina.gob.ar',
    url='https://github.com/jbianchi81/a5_client',
    cmdclass={
        "install": CustomInstallCommand,
    },
    python_requires=">=3.10",
    install_requires=[
        "requests",
        "gdal==3.9.1",
        "numpy",
        "psycopg2",
        "sqlalchemy",
        "geoalchemy2",
        "rasterio",
        "shapely"
    ],
    include_package_data=True
)

