from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vf_tumaini_sacco/__init__.py
from vf_tumaini_sacco import __version__ as version

setup(
	name="vf_tumaini_sacco",
	version=version,
	description="Victory farms employee sacco platform",
	author="willbroad",
	author_email="willbroado@victoryfarmskenya.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
