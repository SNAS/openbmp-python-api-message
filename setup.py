#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages


setup(name='openbmp-python-api-message',
      version='1.0',
      description='This library implements the OpenBMP message',
      url='http://github.com/omerpalaz/openbmp-python-api-message',
      author='opalaz',
      author_email='opalaz@cisco.com',
      license='Eclipse Public License - v 1.0',
      install_requires=[],
      packages=find_packages(exclude=['examples']),
      zip_safe=False)
