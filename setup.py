# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in bondinsurance/__init__.py
from bondinsurance import __version__ as version

setup(
	name='bondinsurance',
	version=version,
	description='Test app',
	author='Bantoo',
	author_email='devs@thebantoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
