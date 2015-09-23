from setuptools import setup, find_packages
from phonenumber_field import __version__


setup(
    name="backend-phonenumber-field",
    version=__version__,
    url='http://github.com/utribo/backend-phonenumber-field',
    description="A Django library which interfaces with python-phonenumbers to validate, pretty print and convert phone numbers.",
    install_requires=[
        'phonenumbers>=7.0.2',
    ],
    long_description=open('README.md').read(),
    author='David Michon',
    author_email='david@utribo.com',
    maintainer='David Michon',
    maintainer_email='david@utribo.com',
    packages=find_packages()
)
