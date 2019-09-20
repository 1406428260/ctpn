from setuptools import setup, find_packages
setup(
	name="ctpn",
	version="1.0",
	description="ocr ctpn module",
	author="piginzoo",
	url="http://www.piginzoo.com",
	license="LGPL",
	packages=find_packages(where='.', exclude=(), include=('*',))
)