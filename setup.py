from os import path
from codecs import open
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='instascraper',
    version='0.1.0',

    description='Instagram bot scripts for promotion and API python wrapper.',
    long_description=long_description,

    author='Steffan Jensen',
    author_email='brominercom@gmail.com',
    license='Apache Software License 2.0',

    url='https://github.com/instagrambot/Instagram-scraper-with-autopost',
    keywords=['instagram', 'bot', 'api', 'wrapper'],
    install_requires=[
        'tqdm>=4.30.0',
        'face_recognition>=1.2.3',
        'instabot>=0.31.0',
    ],
    classifiers=[
        # How mature is this project? Common values are
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Information Technology',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(),
)