#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @ 2016 Ryan Song

import io
try:
    from setuptools import setup
except:
    from distutils.core import setup
import torndsession


def read(*filenames, **kwargs):
    encoding= kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

version = torndsession.version
long_description = read("README.rst")

setup(
    name = 'torndsession',
    version = version,
    description = "Session extensions for Tornado",
    long_description = long_description,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP :: Session',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords='torndsession tornado session redis memcached memory file python',
    author="Ryan.Song",
    author_email="xxx@xxx.com",
    url="http://github.com/mitchellchu/torndsession",
    license="MIT",
    packages = ["torndsession"],
    include_package_data=True,
    zip_safe=True,
    install_requires=['tornado',],
)
