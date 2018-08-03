import codecs
import os
from setuptools import setup

setup(
    name="pyjproperties",
    version="1.0.1",
    description="Java Property file parser and writer for Python",
    # Read the long description from our README.rst file, as UTF-8.
    long_description=codecs.open(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "README.rst"
            ),
            "rb",
            "utf-8"
        ).read(),
    author="Tilman Blumenbach",
    author_email="tilman+pypi@ax86.net",
    entry_points={
        "console_scripts": [
            "propconv = pyjproperties:main"
        ]
    },
    url="https://github.com/globocom/pyjproperties",
    py_modules=["pyjproperties"],
    install_requires=["six>=1.10.0"],
    setup_requires=["pytest-runner ~= 2.0"],
    tests_require=[
        "pytest",
        "pytest-cov",
        "pytest-datadir-ng"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development"
    ],
    license="BSD 3-Clause License; partially licensed under the Python Software Foundation License",
    keywords="java property properties file parser reader writer",
)
