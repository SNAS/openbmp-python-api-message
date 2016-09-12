from setuptools import setup, find_packages

setup(name='openbmp-python-api-message',
      version='1.0',
      description='This library implements the OpenBMP message',
      url='http://github.com/omerpalaz/openbmp-python-api-message',
      author='opalaz',
      author_email='opalaz@cisco.com',
      license='MIT',
      install_requires=[],
      packages=['openbmp', 'openbmp.api', 'openbmp.api.parsed', 'openbmp.api.parsed.message'],
      package_dir={'openbmp': '../src/openbmp', 'openbmp.api': '../src/openbmp/api', 'openbmp.api.parsed': '../src/openbmp/api/parsed', 'openbmp.api.parsed.message': '../src/openbmp/api/parsed/message'},
      zip_safe=False)
