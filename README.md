
# Predicting Cybersickness from Postural Data with Machine Learning
 This project is an initial attempt to develop a model to predict cybersickness based on postural data. The reasoning behind it comes from the postural instability theory. Which states that cybersickness symptons emerge due to a lack of postural control. According to this theory, based on individual postural pattern, it would be possible to predict the ones at a higher risk of suffering from cybersickness. You can see more about the theory and studies related to it in the article we recently published [HERE](https://www.frontiersin.org/articles/10.3389/frvir.2022.1001080/full). 


## Table of Contents

  - [Installation](#installation)
  - [Repository: Folders and Files](#repository-folders-and-files)

## Installation
Firstly, make sure to download the full repository to your local machine.

All the needed libraries can be directly imported using the "requirements.txt" file, using the following code in the terminal:
```python
pip install -r requirements.txt
```
You might find a problem installing the pyts package using pip. If that happens, you can run the following:
```python
git clone https://github.com/johannfaouzi/pyts.git
cd pyts
pip install .
```

After installing the packages, you can directly run the notebook: "data_analysis_and_modeling.ipynb" or firstly, run the pre_processing.py script to generate the datasets and then running the notebook to see the analyses. 

## Repository: Folders and Files
Folders:
- data: This folder contains the raw data used in the analysis. Inside this folder there are three other folders, one for each experiment in which we analyzed the data.
- figures: In this folder you can find all the figures generated in the notebook and in the blog.
- pyts: This is the clone of the pyts repository. This folder is a package and can be used as such. 
- data_analysis_and_modeling.ipynb: This is the main notebook with all the analyses. 
- pre_processing.py: This is a Python script responsible for all the data wrangling and preprocessing.
- requirements.txt: This is the file containing all the libraries needed to run the notebook.
