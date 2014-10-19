#!/usr/bin/env python

# Copyright 2015 Depop Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

install_requires = [
    'sentry>=5.3.3',
    'pygerduty',
]

f = open('README.rst')
readme = f.read()
f.close()

setup(
    name='sentry-pagerduty',
    version='0.0.1',
    author='Depop developers',
    author_email='dev@depop.com',
    url='https://github.com/depop/sentry-pagerduty',
    description='A Sentry plugin for sending error occurrences to a PagerDuty instance.',
    long_description=readme,
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'sentry.plugins': [
            'sentry_pagerduty = sentry_pagerduty.plugin:PagerDutyPlugin'
        ],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development'
    ],
    keywords='sentry pagerduty',
)
