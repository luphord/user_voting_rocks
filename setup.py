#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The setup script.'''

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0',
                'beautifulsoup4>=4.7'
                'jupyter>=1.0',
                'scikit-learn>=0.20',
                'joblib>=0.13']

setup_requirements = []

test_requirements = []

setup(
    author='luphord',
    author_email='luphord@protonmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    description='Use your personal talk voting for PyConDE 2019 to predict your interest in a talk.',
    entry_points={
        'console_scripts': [
            'user_voting_rocks=user_voting_rocks.cli:main',
        ],
    },
    install_requires=requirements,
    license='MIT license',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='user_voting_rocks',
    name='user_voting_rocks',
    packages=find_packages(include=['user_voting_rocks']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/luphord/user_voting_rocks',
    version='0.3.0',
    zip_safe=False,
)
