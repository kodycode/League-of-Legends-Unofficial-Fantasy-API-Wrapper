#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='fantasylcs',
    version='1.1.1',
    url='https://github.com/kodycode/Fantasy-LCS-API-Wrapper',
    author='Kody Thach',
    license='MIT License',
    packages=['fantasylcs'],
    description='An unofficial FantasyLCS API Wrapper.',
    long_description=open('README.md', 'r').read(),
    install_requires=['requests==2.18.4'],
)
