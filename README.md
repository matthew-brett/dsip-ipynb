# Data Science in Practice

Course materials and notes for Data Science in Practice course at the London
Interdisciplinary School.

## Machinery

The template for this website comes from <https://jupyterbook.org> - many
thanks to the authors.

## Getting started for working on the repository

Say your Github username is `my-gh-user`.

Go to the repository page that houses this README - for example
<https://github.co/lisds/dsip>.

Click on "Fork" button near top right, to make your own fork of the
repository, that will now be at `https://github.com/my-gh-user/<repo-name>` where `<repo-name>` is the name of the repository housing this README.

The following assumes that the README is in <https://github.com/lisds/dsip>.
The name of the repository is therefore `dsip`.  Substitute URL and
repository name throughout.

Clone the main repo:

```
git clone https://github.com/lisds/dsip
```

Add a remote for your fork:

```
cd dsip
git remote add my-gh-user https://github.com/my-gh-user/dsip.git
git fetch my-gh-user
```

Get any submodules for the repository (you may need these for the
build):

```
git submodule update --init
```

Install the code modules and build dependencies for this book:

```bash
pip install -e .
```

Start by making some branch to work on, linked to your fork.  Use
a name to match the kind of changes you are about to make, like
`rewrite-intro-pages`:

```
git branch rewrite-intro-pages
git checkout rewrite-intro-pages
```

Associate this branch with your fork:

```
git push my-gh-user rewrite-intro-pages -u
```

The `-u` flag above stores the association of this branch with your
fork, referenced by `my-gh-user`.

## Installing stuff for building / serving the repository files

If you use [Conda](https://conda.io/docs) then you might make a Conda
environment for working on the repo.  I don't, I use pip, and I make
a virtual environment.  You can do that like this:

```
python3 -m venv my-venv
source my-virtualenv/bin/activate
```

Or, if you have
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/stable/)
(I do) then, you might prefer:

```
python3 -m venv $WORKON_HOME/my-venv
workon my-venv
```

Install the Python packages you need for building the site:

```
pip install -r build_requirements.txt
```

Finally, check that you can build the pages locally with:

```
make html
```

## Configuring Jupyter to save / load in R Markdown

I'm using the excellent [Jupytext](https://github.com/mwouts/jupytext)
to make it easier to edit Jupyter Notebooks.  Jupytext automates
saving Notebook files as Markdown (and other formats), and loading
them from edited Markdown (and other formats).

You need to configure Jupyter to use it.  If you don't have a Jupyter
configuration, do:

```
jupyter notebook --generate-config
```

You should now have a file `~/.jupyter/jupyter_notebook_config.py`.
Append these lines:

```
c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"
c.ContentsManager.default_jupytext_formats = "ipynb,Rmd"
```

I also turned off autosave globally, by following the instructions [in
this stackoverflow answer](https://stackoverflow.com/a/45980165).
This stops autosave saving over any edits that I am making in the
Markdown source.

**Be careful** - if you are used to autosave in Jupyter, you can
easily lose work when you disable autosave.

```
mkdir -p ~/.jupyter/custom
```

Add the following line to `~/.jupyter/custom/custom.js`:

```
Jupyter.notebook.set_autosave_interval(0); // disable autosave
```

## Extra stuff

Consider installing [hub](https://github.com/github/hub) to make interactions
with Github easier, from the command line.  Or use the official [gh command
line tool](https://cli.github.com).

## Configuring build etc

You might want to check the instructions for configuring the build at
<https://jupyterbook.org>.

## Workflow

### Developing

* Edit `.Rmd` notebook files.
* `make html` to build textbook files.
* Review in browser

### Shipping

Our continuous integration does this with Github Actions, so the version of the
textbook on Github Pages should correspond to the latest commit (unless Github
Actions failed).  If you have to do the build manually for some reason then
`make github`.
