#!/usr/bin/env python

from setuptools import setup


setup(
    name='Flask-BCS',
    version='0.9.1',
    url='https://github.com/csuzhangxc/Flask-BCS',
    license='MIT',
    author='Zhang Xuecheng',
    author_email='csuzhangxc@gmail.com',
    description='Baidu Cloud Storage for Flask',
    long_description='Baidu Cloud Storage for Flask. Please visit: https://github.com/csuzhangxc/Flask-BCS',
    py_modules=['flask_bcs'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    keywords='bcs for flask',
    packages=['pybcs'],
    package_data={'': ['LICENSE']},
    install_requires=[
        'setuptools',
        'Flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
