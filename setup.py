#!/usr/bin/env python
# coding: utf-8
import json

import time
from setuptools import setup

version_ = "0.0.1a400"

setup(
    name='ezcaptcha',
    version=version_,
    author='JiangCX',
    author_email='jcx03@outlook.com',
    url='https://github.com/JiangCX3/Ezcaptcha',
    description='Python easy generate captcha images in one sentence.',
    packages=['ezcaptcha'],
    install_requires=['numpy', 'Pillow']
)
