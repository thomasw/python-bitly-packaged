#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(name="bitly",
      version="0.2.2",
      description="Bit.ly library for python",
      license="Apache License 2.0",
      author="Yoav Aviram",
      author_email="info@matchstrike.net",
      url="http://github.com/thomasw/python-bitly-packaged",
      install_requires=["simplejson",],
      packages = find_packages(),
      keywords= "bitly",
      zip_safe = False)