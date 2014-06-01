from distutils.core import setup
from setuptools import find_packages

setup(
    name="memplot",
    version="0.1.1",
    author="Eric Chiang",
    author_email="eric@yhathq.com",
    url="https://github.com/EricChiang/memplot",
    packages=find_packages(),
    description="Plot the mememory usage of a process",
    license="MIT",
    scripts=['bin/memplot'],
    install_requires=[
        "docopt==0.6.1",
        "matplotlib==1.1.1",
        "psutil==2.1.1"
    ]
)
