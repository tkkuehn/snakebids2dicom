#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['snakebids @ git+https://github.com/akhanf/snakebids.git@90b8a14bb4245e7a69d25745062848bef7a6182a',
                    pydicom ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Tristan Kuehn",
    author_email='tkuehn@uwo.ca',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Convert 3D niftis to dicom",
    entry_points={
        'console_scripts': [
            'snakebids2dicom=snakebids2dicom.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='snakebids2dicom',
    name='snakebids2dicom',
    packages=find_packages(include=['snakebids2dicom', 'snakebids2dicom.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tkkuehn/snakebids2dicom',
    version='0.1.0',
    zip_safe=False,
)
