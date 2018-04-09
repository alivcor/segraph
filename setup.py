from distutils.core import setup

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='segraph',
    packages=['segraph'],  # this must be the same as the name above
    version='0.5',
    description='Creates graphs with edges and vertices from SLIC segments. Can be used with PyStruct library for image segmentation using CRF.',
    author='Abhinandan Dubey',
    author_email='abhinandandubey@live.com',
    url='https://github.com/alivcor/segraph',  # use the URL to the github repo
    license='GNU General Public License v3 (GPLv3)',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],
    download_url='https://github.com/alivcor/segraph/archive/0.5.tar.gz',  # I'll explain this in a second
    keywords=['segmentation', 'image', 'crf', 'pystruct'],  # arbitrary keywords
)
