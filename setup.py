# -*- coding: utf-8 -*-
# Date: 2019/1/15


import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='example_pkg',
    version='1.0',
    author='Anthony Wang',
    author_email='tingyuweilou@163.com',
    license='GPL',
    keywords=('example_pkg', 'Wahaha'),
    desciption='test example_pkg',
    long_description=long_description,
    long_description_type='text/markdown',
    packages=setuptools.find_packages(),
    url='https://github.com/WZSwang/test_distribute_package.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)


