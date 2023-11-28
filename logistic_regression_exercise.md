In this exercise you will perform some simple logistic regression analysis using
the new workflow (e.g. using the command line, scripts, git and github).

- Get into teams of 2 or 3 people (smaller groups are better, no more than 3
  per group)
- One person creates a github repository called "logistic_regression_analysis"
- Download the full CKD dataset into the repository, from here: https://github.com/matthew-brett/cfd2020/blob/master/data/ckd_full.csv
- Everybody in the group (including the person who created the repository)
  creates a fork of the repository, on their own github account

Your task (as a group) is to fit the following logistic regression model
`Class ~ Hemoglobin`. E.g. predicting whether or not a patient has CKD from
their hemoglobin score.

To do this you should write the following set of scripts (**as much as possible,
you should each work on separate parts of the analysis, and collaborate via
pull requests**):

- DATA CLEANING SCRIPT: a .py file to perform you data cleaning (e.g. creating
  the dummy codes for `Class`). Use `df.to_csv()` to save your clean data to
  a csv file with a different filename to the original file name.

- COST FUNCTION SCRIPT: create a .py file containing the logit transformation
 function, the inverse logit transformation function, and the logistic regression
 cost function. DO NOT COPY/PASTE the functions from the textbook page, try to
 re-write them line-by-line yourselves so you understand what each line is doing.
 These functions can then can imported by other scripts in the repository, e.g.
 if this file is called "cost_function_utils.py" then you can import the
function into other scripts using `import cost_function_utils`

- DATA ANALYSIS SCRIPT: this .py file should do several things:
        - First, this script should plot `Class` as a function of `Hemoglobin`. 
        - Then the script should fit your model (`Class ~ Hemoglobin`) using
         `minimize` (by importing your cost function from COST FUNCTION SCRIPT). 
        - You should then fit the same model using statsmodels.
        - You should write some tests to check that `minimize` and `statsmodels`
          are producing similar parameter estimates (HINT: you may want to investigate
         `np.isclose()` and `assert` - ask us for help with this also).
        - You should then create a new plot, showing `Class ~ Hemoglobin`, but 
        also showing the predictions from your logistic regression model.

If you want to, you can create a Jupyter Notebook to show the results of your
data analysis script. You can use an .Rmd or .ipynb file here, as the notebook
will only contain a few lines (see the example `showcase_notebook.ipynb`)

An example repo, with some blank templates, can be found here: https://github.com/lisds/logistic_regression_exercise