MSE Exposure Time Calculator (Flagey, ver2020)
============================================================

[![Python: 3.6](https://img.shields.io/badge/Python->3.6-blue.svg)](#)
		
Code developers and contributors
---------------------------------
The original ETC was written and developed by Nicolas Flagey (formerly, CFHT, currently, STScI; nflagey@stsci.edu) and
modified by him in subsequent years through 2020 (modifications were
done to accommodate potential instrument design changes).

Slight code alterations and GitHub repository building done by
Jen Sobeck (CFHT; sobeck@cfht.hawaii.edu).


Release Notes
------------
* Version 1.0.0  (2020; main code modifications by NF)
* Version 1.0.1  (2022; minor code changes by JS)

Requirements
------------
* Python3 (recommended as Python2 is not really supported)
* scipy 
* numpy
* astropy
* matplotlib
* bokeh

Installation
------------
To install the package, retrieve the associated git repository and type
the following: 
  
    git clone https://github.com/mse-cfht/etc_flagey_ver2020.git
    cd etc_flagey_ver2020
    python setup.py install


Description
-----------
The MSE ETC ver2020 has two calculation methods: signal-to-noise (SNR)
and exposure time. 

At the CLI, the ETC can be run as follows:

    python run_etc.py 

This version of the ETC does not have an active web API.
