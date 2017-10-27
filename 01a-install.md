# Install software on your computer


### Install [git](http://git-scm.com/).

You have it installed if you can run `git --version` at the command
line and get output like `git version 2.3.5`.


### Install [Anaconda](http://continuum.io/downloads).

There are two things you can verify to check your install.

First, from the command line, all of the following should start up
some kind of Python interpreter:

```bash
python
ipython
ipython notebook
spyder
```

Second, inside any of those Python interpreters, you should be able to
do all of these without error:

```python
import numpy
import scipy
import matplotlib
import pandas
import statsmodels
import sklearn
```

### Install [Homebrew](http://brew.sh/) on Mac

If you use a Mac, install Homebrew if you don't
have it yet. You could use Homebrew to manage your `git` and `python`
installs as well, but the methods given above are very good and more
cross-platform.

---

### Q1. Python Version 2 or 3

**Course material for the bootcamp is compatible with Python versions 2.7 and 3.0. All HackerRank Python pre-work is configured for Python 3 only.  Therefore, Python 3 is the recommended version.**  

Did you install Python 2 or 3? Why?  

My default is Python 3, but I also have Python 2 on my computer.  That way I have both.

### Q2. Which Python Version Installed   

How can you check the version of Python installed if you happen to be on an unfamiliar computer?

Enter the command `python -V`. Or just the command `python`, and the environment will list its version on the line below where you entered that command.
