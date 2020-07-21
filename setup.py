#!/usr/bin/env python

from setuptools import setup

setup(name='Covid Twitter ETL',
      version='1.0',
      description='Import Twitter API data for analysis comparison to Covid timeline.',
      author='Ian Mitchell',
      author_email='iancharlesmitchell@gmail.com',
      url='https://github.com/iancmitchell/covid-twitter-analysis',
      packages=['twitter_client','tests','credentials'],
      py_modules=['main']
     )




