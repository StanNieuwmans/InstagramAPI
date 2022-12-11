from setuptools import setup
from os import path
from codecs import open


# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='python-InstagramBusinessAPI',
    version='0.1.0',
    description='Instagram Business API to POST content to Instagram',
    author='Stan Nieuwmans',
    author_email='snieuwmans@gmail.com',
    url='https://github.com/StanNieuwmans/InstagramAPI',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'requests',
    ],
    packages=['InstagramAPI'],
)
