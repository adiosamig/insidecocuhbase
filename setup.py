from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name='insidecouchbase',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/adiosamig/insidecocuhbase',
    author='Huseyin Demir',
    author_email='huseyin.d3r@gmail.com',
    description='Check cluster healt and best practices on production Couchbase.',
    install_requires=[
        'requests',
        'tabulate',
        'pandas'
    ]
)