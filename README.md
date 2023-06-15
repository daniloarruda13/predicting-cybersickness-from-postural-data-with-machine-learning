
# Predicting Cybersickness from Postural Data with Machine Learning <!-- omit in toc -->
 This project is an initial attempt to develop a model to predict cybersickness based on postural data. The reasoning behind it comes from the postural instability theory. Which states that cybersickness symptons emerge due to a lack of postural control. According to this theory, based on individual postural pattern, it would be possible to predict the ones at a higher risk of suffering from cybersickness. You can see more about the theory and studies related to it in the article we recently published [HERE](https://www.frontiersin.org/articles/10.3389/frvir.2022.1001080/full). 


## Table of Contents <!-- omit in toc -->


- [Installation](#installation)
- [Repository: Folders and Files](#repository-folders-and-files)
- [Motivation](#motivation)
- [Summary of results](#summary-of-results)
- [Data Usage Notice](#data-usage-notice)
- [Contact information](#contact-information)

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

## Motivation

Currently, virtual reality (VR) is one of the hottest topics in technology. Cybersickness, however, represents one of the largest concerns of the industry. This condition is characterized by the same symptoms as motion sickness, including nausea, dizziness, disorientation, headaches, sweating, fatigue, and eye strain. The prevalence of these symptoms varies between 20 and 45%, with females having a higher incidence. While the etiology of that discomfort has been extensively studied, no consensus has been reached regarding its causes. My belief is that we fail to stabilize our bodies, resulting in cybersickness. The postural instability theory is based on this concept. You can see more about the theory and studies related to it in the article we recently published [HERE](https://www.frontiersin.org/articles/10.3389/frvir.2022.1001080/full)

Consequently, analyzing how people control their posture may provide some insight into who is more likely to experience motion sickness. The purpose of this article is to examine the relationship between cybersickness and posture. Specifically, we will examine machine-learning models trained with real-world data to determine if those models can be used to predict cybersickness. This is relevant because if we are able to predict people who will become sick in a virtual environment, then we may be able to develop specific strategies to mitigate cybersickness before the user becomes sick.

## Summary of results

In conclusion, our analysis of the different models used in this study reveals that the time series models outperformed the discrete models in terms of predictive accuracy. However, it is important to consider the limitations of the dataset, particularly its size and the variation in data sources due to different experiments.

The superiority of the time series models highlights the importance of capturing temporal patterns and dependencies in the data for accurate predictions. Leveraging the sequential nature of the time series data provided a more comprehensive understanding of the underlying patterns, resulting in improved model performance.</

In light of the constraints posed by our analyses and datasets, we have successfully demonstrated the feasibility of utilizing motion data to predict cybersickness prior to individuals entering VR. This finding holds immense significance as it enables VR developers to design a preliminary application that identifies individuals susceptible to cybersickness before engaging in VR experiences. This proactive approach empowers developers to implement tailored strategies for cybersickness mitigation, thereby enhancing the overall user experience and ensuring user comfort and safety during VR interactions.


## Data Usage Notice

The data used in this project is the property of Affordance Perception-Action Laboratory. It is not to be published, shared, or distributed without explicit authorization. This data is provided solely for the purpose of transparency when generating the models.
If you are interested in using this data, please contact me to request permission and obtain the necessary authorization.
Any unauthorized use or distribution of this data is strictly prohibited and may result in legal action.

## Contact information

This project is an initial effort in developing predictive models for cybersickness. If you want to collaborate and help, please reach out to my email at daniloarruda13@gmail.com.