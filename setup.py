import setuptools
import os

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "README.md"), "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sse-numbers",
    version="0.1.0",
    author="Federico A. Galatolo",
    author_email="federico.galatolo@ing.unipi.it",
    description="",
    url="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    classifiers=[
    ],
)
