#!/usr/bin/env python
# coding: utf-8
import json

from setuptools import setup

version = "0.0.1"
tag = "-alpha"

f = open("version.json", "w").write(json.dumps({
    "version": version,
    "tag": tag
}))

setup(
    name='ezcaptcha',
    version=version,
    author='JiangCX',
    author_email='jcx03@outlook.com',
    url='https://github.com/JiangCX3/Ezcaptcha',
    description='Python easy generate captcha images in one sentence.',
    packages=['ezcaptcha'],
    install_requires=['numpy', 'Pillow']
)
