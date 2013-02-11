# Getting Started With Python

Document the process followed to get to know python

## Good Reads
List suggested in [python wiki] [3]

Interesting  Guide at [tutorialspoint] [4] providing installation instructions and thorough description of the language features


## Which Python Version to choose
There is an [article] [2] describing pros and cons of using Python 2.x or Python 3.x

Moved with 2.x since its more main stream, keeping an eye on the changes introduced in 3.x to make a later migration easier.


## Set up development environment
### Install python 
The following script was used to install python from sources on Ubuntu 12.04
```
sudo apt-get install build-essential &&
cd /tmp && 
wget http://python.org/ftp/python/2.7.3/Python-2.7.3.tgz &&
tar -xvf Python-2.7.3.tgz && cd Python-2.7.3/ &&
./configure &&
make &&
sudo make altinstall
```

## Resources
[1]: http://python.org/ "Official Python Site"
[2]: http://wiki.python.org/moin/Python2orPython3 "Python 2 or 3?"
[3]: http://wiki.python.org/moin/BeginnersGuide/Programmers "Tutorials/Websites/Books"
[4]: http://www.tutorialspoint.com/python/index.htm "Getting Started Guide"
