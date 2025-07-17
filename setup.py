from setuptools import setup
from io import open
from os import path
import sys

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="databricksx12",
    version="0.0.5",
    # python_requires='>=3.9.*',
    python_requires='>=3.9',
    author="X12",
    author_email="aar@databricks.com",
    description= "Parser for handling x12 EDI transactions in Spark",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    # url="https://github.com/databricks-industry-solutions/x12-edi-parser",
    url="https://github.com/shaker-p/x12-edi-parser-test",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    packages=['databricksx12', 'databricksx12.hls'],
    py_modules=['databricksx12'],
    extras_require={
        'test': [
            'pyspark>=3.4.0',
            'pytest>=7.0.0',
            'pytest-spark>=0.6.0'
        ]
    }
)
