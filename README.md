# Pepper

## Install Python SDK in Linux (bash)

1) Fetch the proper Python package from https://community.ald.softbankrobotics.com/en/resources/software/language/en-gb/field_software_type/sdk

2) Unpack the tar file, for example in your home directory
 > pwd /home/ervajn
 > tar xvf pynaoqi-python2.7-2.5.5.5-linux64.tar.gz 

3) Set the environment variable PYTHONPATH to poin to site-packages in the sdk
 > export PYTHONPATH=${PYTHONPATH}:/home/ervajn/pynaoqi-python2.7-2.5.5.5-linux64/lib/python2.7/site-packages

4) Test it:
 > python
 Python 2.7.14 (default, Oct 26 2017, 14:28:27) 
 [GCC 4.8.2] on linux2
 Type "help", "copyright", "credits" or "license" for more information.
 >>> import naoqi
 >>> 
