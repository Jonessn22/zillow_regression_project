# Beating the Zillow Zestimate® for Home Values
Stephanie N. Jones<br>
Data Scientist<br>
Monday, December 13, 2021<br>
Codeup | Hopper Cohort<br> 

## Project Summary
>For most consumers, a home is the largest purchase they will make over the course of their lifetime. Ensuring consumers have a trusted way to monitor a home’s value is vital. The Zestimate® estimates home values based on 7.5 million statistical and Machine Learning models that analyze hundreds of data points on each property and marks the first time consumers have had access to this valuation information at no cost. Zillow has since become established as one of the most trusted real estate information marketplaces in the U.S. and a leading example of the power and value of machine learning.[^2]

>For this project I will be performing the role of a Junior Data Scientist on the Zillow Data Science Team, working to improve Zillow's current Zestimate® by finding drivers of homes' tax assessed value and creating a Machine Models that predict the values of single family homes with transactions in 2017.[^3]

Audience
>Zillow Data Science Team

Deliverables<br>
- Final Report and Presentation<br>
- Github Repository with README.md and reproducible project files<br>
- Python Function Modules (acquire.py and prepare.py, at minimum)<br>
- Data Dictionary<br>

Steps to Reproduce<br>
:white_check_mark: Read this README.md file<br>
:white_large_square: Create .env file with SQL Database credentials and ignore file<br>
:white_large_square: Clone this repo and use .py modules in your file to access functions<br>

## Business Goals
#### Primary Goal 1 | Predict Home Values
>Construct Machine Learning model by finding key drivers that predicts property tax assessed values ‘taxvaluedollarcnt’ of Single Family Properties with transactions during 2017 
#### Primary Goal 2 | Beat Zestimate®
>Improve existing Zillow model for predicting home values 
#### Secondary Goal | Property Locations
>City and state of each property

## Executive Summary
#### Initial Questions and Hypothesis
> Question 1<br>
Question 2<br>
Question 3<br>
Question 4

>Initial Hypothesis

#### Conclusions
>Conclusions

>Key Findings

>Recommendations

>Takeaways

## Process | Data Science Pipeline
### 00 Planning
>[Trello Board](https://trello.com/b/a7550YvK/zillowregressionproject)

>[Project Outline](https://docs.google.com/document/d/1NHzrmd0hoA4AoQd8Ct4I3GhuBJHtTpCqZyr8Aw_e6wI/edit?usp=sharing)

### 01 Acquire Data

### 02 Prepare Data (for Exploratory Analysis)
1. Import libraries, modules, and functions
2. Clean data
    - Column names
    - Drop nulls
    - Drop 0 counts
    - Remove outliers
3. Create global variables for column groups
4. Visualize boxplots of data
    - Top row: before outliers removed
    - Bottton row: after outliers removed
5. Split and prepare data for modeling

### 03 Explore Data

### 04 Create ML Models

### 05 Evaluate ML Models

### 06 Test and Conclusions

##### References
[^1]: Zillow website | About Zestimate®. https://www.zillow.com/z/zestimate/ 
[^2]: Kaggle website | Zillow Competition. https://www.kaggle.com/c/zillow-prize-1 
[^3]: Codeup project specs | Codeup Data Science Course Catalogue. https://codeup.com/ds-course-catalog/
