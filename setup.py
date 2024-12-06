from setuptools import setup, find_packages
from setuptools.command.install import install

import subprocess

# Get GDAL version
def get_gdal_version():
    result = subprocess.run(["gdalinfo", "--version"], stdout=subprocess.PIPE, text=True)
    return result.stdout.split()[1].rstrip(",")  # Extract version (e.g., "3.8.4")

class CustomInstallCommand(install):
    def run(self):
        try:
            # Use GDAL version in a pip command
            gdal_version = get_gdal_version()
            subprocess.run(["pip", "install", f"gdal=={gdal_version}"])
            # create_ini_from_dict(config_data, config_path)
            print(f"GDAL Version Detected: {gdal_version}")
        except Exception as e:
            raise RuntimeError(f"Error detecting GDAL version: {e}")
        super().run()

setup(
    name="a5py",
    version="0.1.1",
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
        "gdal",
        "numpy",
        "psycopg2",
        "sqlalchemy",
        "geoalchemy2",
        "rasterio",
        "shapely"
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'a5py=a5py.a5py_cli:main',
            'a5py_config=a5py.config:run',
        ],
    },
)

