from setuptools import setup

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/dikshasethi2511/cloud-pip-package',
    author='Diksha Sethi',
    author_email='diksha20056@iiitd.ac.in',

    py_modules=['my_pip_package'],
)