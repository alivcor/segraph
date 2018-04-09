
[![DOI](https://zenodo.org/badge/92789575.svg)](https://zenodo.org/badge/latestdoi/92789575)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/alivcor/segraph)
[![dependencies Status](https://david-dm.org/boennemann/badges/status.svg)](https://github.com/alivcor/segraph)
[![Build Status](https://travis-ci.org/alivcor/segraph.svg?branch=master)](https://travis-ci.org/alivcor/segraph)

<p align="center">
<img src="logo.png"/>
</p>


The segraph library provides modules for creating graphs from SLIC segments. This can be used with PyStruct library for image segmentation using CRF.

<a href="https://github.com/alivcor/segraph">:octocat: Link to GitHub Repo</a>

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See examples to see a quick example.

### Prerequisites

You will need to have NumPY installed on your system. The segraph library was built with Python 2.7, keeping in mind the stability with Python 3+, but it is not guranteed.

```
pip install numpy
```

### Installation

There are multiple ways to install segraph on your system:

#### Python Package Index

segraph is now available at https://pypi.python.org/pypi/segraph/0.5



```
1. Download the tar/zip from https://pypi.python.org/pypi/segraph/0.5
2. Move the package to your desired location / python version, and unzip the archive. 
Optionally, if you have a linux-based machine (Ubuntu/OSX):
      tar xvzf segraph-0.x.tar.gz -C /path/to/desireddirectory
3. Migrate to the segraph folder, and run
      python setup.py install
```

#### Using pip

```
pip install segraph
```

To upgrade,

```
pip install --upgrade segraph
```


## Using segraph

segraph can be very helpful for creating graphs from SLIC segmented images (superpixels). Here is an example usage:

```
from skimage.segmentation import slic
from skimage.util import img_as_float
from skimage import io as skimageIO
from segraph import create_graph
import numpy as np

image = img_as_float(skimageIO.imread("segraph/data/flowers.png"))
segments = slic(image, n_segments=500, sigma=1.0)
# Create graph of superpixels 
vertices, edges = create_graph(segments)

# Compute centers:
gridx, gridy = np.mgrid[:segments.shape[0], :segments.shape[1]]
centers = dict()
for v in vertices:
    centers[v] = [gridy[segments == v].mean(), gridx[segments == v].mean()]

```

segraph can be used with PyStruct library for image segmentation using CRF.


## Contributing

You are welcome to send a pull-request.

## Contributors

Thanks to all the contributors for making it even more awesome !

- @pinkfloyd06

## Authors

* **Abhinandan Dubey** - *@alivcor* - [Human Interaction Lab, Stony Brook University](https://www.cs.stonybrook.edu/~adubey)


## License

This project is licensed under the GNU General Public License v3 - see the [LICENSE.md](LICENSE.md) file for details

[![forthebadge](http://forthebadge.com/images/badges/makes-people-smile.svg)](https://github.com/alivcor/segraph/#)

