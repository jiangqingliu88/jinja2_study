# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

"""
打包的用的setup必须引入，
"""

VERSION = '0.0.1'

setup(name='pycase',
      version=VERSION,
      description="a command line tool for camel case",
      long_description='a python command tool for camel case',
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='pycase',
      author='Peng Shiyu',
      author_email='pengshiyuyx@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[],
      entry_points={
          'console_scripts': [
              'pycase = pycase.case:main'
          ]
      }
      )

#
# pycase = pycase.case:main

#相当于
#pycase == pycase/case.py.main

#其中，main 是定义好的main() 方法

