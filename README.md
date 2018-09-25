# Pepper

## Install Python virtual environment (Linux, bash)

1) Fetch the virtual environment code and unpack it
```
> cd /home/${USER}
> wget https://files.pythonhosted.org/packages/33/bc/fa0b5347139cd9564f0d44ebd2b147ac97c36b2403943dbee8a25fd74012/virtualenv-16.0.0.tar.gz
> tar xvf virtualenv-16.0.0.tar.gz
```

2) Install the virtualenv, for example in a directory in in the home directory
```
> python virtualenv-16.0.0/virtualenv.py venv27
```

3) Activate the virtual environment and verify that it works
```
> source venv27/bin/activate
> which python
/home/${USER}/venv27/bin/python
```

## Install Python Pepper SDK (Linux, bash)

1) Fetch the proper Python package from https://community.ald.softbankrobotics.com/en/resources/software/language/en-gb/field_software_type/sdk

2) Unpack the tar file, for example in your home directory
```
> cd /home/${USER}
> tar xvf pynaoqi-python2.7-2.5.5.5-linux64.tar.gz 
```

3) Set the environment variable PYTHONPATH to poin to site-packages in the sdk
```
> export PYTHONPATH=${PYTHONPATH}:/home/${USER}/pynaoqi-python2.7-2.5.5.5-linux64/lib/python2.7/site-packages
```

4) Test it:
```
> python
Python 2.7.14 (default, Oct 26 2017, 14:28:27) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import naoqi
>>> 
```
