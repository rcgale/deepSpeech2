import os
import configparser
from setuptools import setup, find_packages


VERSION = '0.0.1'

setup(
    name='ymdeepspeech2',
    version=VERSION,
    description='Deep Speech 2 tensorflow implementation',
    author='Lakshmi Krishnan',
    author_email='lkrishn7@ford.com',
    url='https://github.com/yao-matrix/deepSpeech2/blob/gpu/src/custom_ops.py',
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=[
    ]
)

