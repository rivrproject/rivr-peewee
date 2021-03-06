#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='rivr-peewee',
    version='0.2.1',
    description='rivr integration for the peewee database ORM.',
    url='https://github.com/rivrproject/rivr-peewee',
    packages=find_packages(),
    install_requires=[
        'rivr',
        'peewee'
    ],
    author='Kyle Fuller',
    author_email='kyle@fuller.li',
    license='BSD'
)

