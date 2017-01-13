#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pitronics',
    version='0.0.1',
    description='Provides simple api for programing various electronics using GIPO pins on Raspberry Pi',
    author='Luke Shiner',
    author_email='luke@lukeshiner.com',
    url='https://github.com/axevalley/pitronics',
    keywords=['electronics', 'GPIO', 'raspberry pi'],
    install_requires=[],
    packages=find_packages(),
    )
