from distutils.core import setup, Extension
from setuptools import setup, Extension

config = {
    'include_package_data': True,
    'description': 'factoring out code from av_scripts',
    'url': 'NA',
    'download_url': 'https://github.com/kundajelab/avutils',
    'version': '0.1',
    'packages': ['avutils'],
    'setup_requires': [],
    'install_requires': [], #gzip, re...blah
    'scripts': ["scripts/make_hdf5", "scripts/shuffle_corresponding_lines"],
    'name': 'avutils'
}

if __name__== '__main__':
    setup(**config)
