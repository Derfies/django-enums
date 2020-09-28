#!/usr/bin/env python3

import os, re
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

if __name__ == "__main__":
    setup(
        name = 'django-enums',
        version='0.0.1',
        description = 'Backport of Django 3.0 enumeration types for model field choices.',
        long_description = README,
        classifiers = [
            "Programming Language :: Python",
            "Framework :: Django",
        ],
        author = 'Matt Pryor',
        author_email = 'matt.pryor@stfc.ac.uk',
        url = 'https://github.com/mkjpryor-stfc/django-enums',
        keywords = 'web django enum enumeration types backport',
        packages = find_packages(exclude = ["tests"]),
        include_package_data = True,
        zip_safe = False,
        install_requires = ['django'],
    )
