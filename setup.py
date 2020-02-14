#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='ezcaptcha',
    version='0.0.1',
    author='JiangCX',
    author_email='jcx03@outlook.com',
    url='https://github.com/JiangCX3/Ezcaptcha',
    description='Python easy generate captcha images in one sentence.',
    packages=['ezcaptcha'],
    install_requires=['numpy', 'Pillow']
)
