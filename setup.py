#!/usr/bin/env python
# # coding: utf-8

from distutils.core import setup


setup(
    name='autojenkins',
    description='Jenkins Remote Control Library',
    version='0.1',
    author='Carles Barrobés',
    author_email='carles@barrobes.com',
    packages=['autojenkins'],
    requires=['requests', 'jinja2'],
)
