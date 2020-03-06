#!/usr/bin/env python3

# Copyright (c) 2020 Fabrice Laporte - kray.me
# The MIT License http://www.opensource.org/licenses/mit-license.php

import os
import time

from setuptools import setup

VERSION = '0.0.2-dev'
DIRPATH = os.path.dirname(__file__)

# Deploy with
# python3 setup.py sdist bdist_wheel; twine upload --verbose dist/*
setup(name='slackerade',
    version=VERSION if not VERSION.endswith('dev') else '%s%s' % (VERSION, int(time.time())),
    description='Masquerade yourself as a fictitious user on slack',
    long_description=open(os.path.join(DIRPATH, 'README.rst')).read(),
    author='Fabrice Laporte',
    author_email='kraymer@gmail.com',
    url='https://github.com/KraYmer/slackerade',
    license='MIT',
    platforms='ALL',

    packages=[
      'slackerade',
    ],
      entry_points={
          'console_scripts': [
              'slackerade = slackerade:slackerade_cli',
          ],
    },
    install_requires=open(os.path.join(DIRPATH, 'requirements.txt')).read().split('\n'),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat',
    ],
    keywords='Masquerade yourself as a fictitious user on slack',
    python_requires='>=3.5.0',
    )
