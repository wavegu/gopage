from setuptools import setup, find_packages

PACKAGE = "gopage"
NAME = "gopage"
DESCRIPTION = "search pages using search engines"
AUTHOR = "xiaotao gu"
AUTHOR_EMAIL = "wavegu@126.com"
VERSION = '1.0'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    zip_safe=False,
)