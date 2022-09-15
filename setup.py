#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='etc_flagey_2020',
      version='1.0.1',
      description='MSE Exposure Time Calculator (ETC) ver2020',
      author='Nicolas Flagey, Jennifer Sobeck',
      author_email='nflagey@stsci.edu',
      url='https://github.com/mse-cfht/etc_flagey_ver2020',
      packages=find_packages(exclude=["tests"]),
      requires=['numpy','astropy','scipy','bokeh','matplotlib'],
      include_package_data=True,
)


