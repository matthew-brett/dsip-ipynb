# Installing on your computer

We are going to be using the following major software for the class:

- [Python](https://python.org)
- [Numpy](https://numpy.org) (the Python array package);
- [Pandas](https://pandas.pydata.org) (Loading and manipulating data);
- [Matplotlib](https://matplotlib.org) (Standard plotting package);
- [Scipy](https://scipy.org) (Python scientific library);
- [Statsmodels](https://www.statsmodels.org) (Statistical models in Python);
- [Scikit-learn](https://scikit-learn.org) (Standard machine-learning tools);

For the class and homework we will use:

- a text editor of your choice - see {doc}`choosing_editor`.  Choosing an
  editor is an important and personal decision, and one we recommend you invest
  some time in.
- the [git](https://git-scm.com/) version control system.

## Installation

:::{note}

It is common to run into problems with installation - don't worry, we're
expecting that.  One of the things we are teaching in this class is how to
solve problems like installing and using scientific software.  So, if you run
into trouble - great - that will be a good opportunity for us to work together
on a not-trivial problem.

:::

Here are the instructions for installing Git and Python:

- {doc}`installation_on_mac`;
- {doc}`installation_on_linux`;
- {doc}`installation_on_windows`.

Next, open Terminal (Mac) or Powershell (Windows) or a terminal of your choice
on Linux.

We suggest you start the steps below in the `Documents` directory in your home
(user) directory.  To make sure you are working in that directory, run this
command in the terminal.

```
cd $HOME/Documents
```

```{warning}
If you get `The system cannot find the path specified`, and you are on Windows,
make sure you are running a **Powershell** shell, not the much older Windows `cmd` shell.
```

Make a new directory to store your work:

```
mkdir dsip-work
```

Change your shell to that directory:

```
cd dsip-work
```

Confirm you are in the right directory with:

```
pwd
```

This Prints the Working Directory (pwd).  You should see something like the following:

::::{tab-set}

:::{tab-item} Windows Powershell
```
Path
----
C:\Users\your-user\Documents\dsip-work
```
:::

:::{tab-item} Mac
```
/Users/your-user/Documents/dsip-work
```
:::

:::{tab-item} Linux
```
/home/your-user/Documents/dsip-work
```
:::

::::

Now, in the terminal, check you have Python installed:

```
python3 --version
```

This should show you the Python 3 version report, something like this:

```
Python 3.10.4
```

Check you have the Python package manager installed:

```
pip3 --version
```

This should show you something like this:

```
pip 22.0.4 from <some-directory/site-packages/pip (python 3.10)
```

Next,  get a copy of all the textbook files:

```
git clone https://github.com/lisds/dsip
```

Change directory to the new textbook directory:

```
cd dsip
```

Confirm you are in the `dsip` textbook directory `pwd` (Print Working Directory):

```
pwd
```

## Making sure you can see your new commands

You are about to install many Python libraries.  Some of these libraries will install commands (scripts) that you can run at the terminal.

You need to make sure that your new commands, installed in the installation step, are available at the terminal.

To do this, run the following command from the `dsip` directory (as above):

```powershell
python3 configure_shell.py
```

You should see the instruction to close your Powershell terminal, and open
it again to see the changes.  Do this.

## Install libraries and commands

Check that the `requirements.txt` file came down with the rest of the textbook files with:

```
ls requirements.txt
```

The `requirements.txt` file has a list of the Python packages to install for the class.

Now finish the Python part of the install with:

```
pip3 install --user -r requirements.txt
```

:::{note}

If you see warnings like this:

```
WARNING: The script <some-program> is installed in 'C:\Users\scipy\AppData\Roaming\Python\Python310\Scripts' which is not on PATH.
```

Then go back and make sure you have run the `python3 configure_shell.py`
command above, and you've closed all terminals, and opened a new one.

:::

## Checking the installation

Keep the terminal open.

Finally, check that your installation has worked correctly by running the `check_install.py` file included with the textbook files.

Start by looking for the `check_install.py` file in your working directory
(`dsip`) with:

```
ls check_install.py
```

from your terminal.  You should see something like:

::::{tab-set}

:::{tab-item} Windows Powershell
```
    Directory: C:\Users\your-user\Documents\dsip-work\dsip


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          4/6/2022   5:04 AM           1937 check_install.py
```
:::

:::{tab-item} Mac or Linux
```
check_install.py
```
:::

::::

Now check your installation has succeeded with:

```
python3 check_install.py
```

You should see something like:

```
Platform: macOS-12.3.1-x86_64-i386-64bit
Python version: 3.8.13 (default, Mar 16 2022, 20:38:07) 
[Clang 13.0.0 (clang-1300.0.29.30)]

Congratulations, all checks passed
```

where the details in the first three lines will depend on your system.

You should now be able to open the textbook notebooks with:

```
jupyter lab
```

from the `dsip` textbook directory. This will open your web browser in the
Jupyter interface.  Select the file you are interested in.
