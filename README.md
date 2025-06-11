
# End to End ML Project Chennai House Price Prediction

## Problem statement
- Develop a machine learning model to accurately predict residential property prices across 7 districts of Chennai, leveraging historical and geographical data to assist buyers, sellers, and real estate stakeholders in making informed decisions

## Steps followed for this Machine Learning Project
- Understanding the Problem Statement
- Dataset
- Data Checks to perform
- Exploratory Data Analysis
- Data Pre-Processing
- Model Training
- Selecting the best model
  

## Sequence of steps followed until Deployment
- Github and Code Set Up
- Project Structure, Logging And Exception Handling
- Project Problem Statement, EDA And Model Training
- Data Ingestion
- Data Transformation using Pipelines
- Model Training and Model Evaluating Component
- Model Hyper Parameter Tuning
- Created Prediction Pipeline using Flask Web App

## Deployment
- Deployment using elastic beanstalk and a CD CodePipeline to [this repository](https://github.com/VishweshJagadeesh/student-deployment) using AWS

## Dataset
- Dataset Source - https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977
- The data consists of 8 column and 1000 rows.

## Dataset information
- gender : sex of students -> (Male/female)
- race/ethnicity : ethnicity of students -> (Group A, B,C, D,E)
- parental level of education : parents' final education ->(bachelor's degree, some college, master's degree, associate's degree, high school)
- lunch : having lunch before test (standard or free/reduced)
- test preparation course : complete or not complete before test
- math score
- reading score
- writing score

## Data Checks Performed
- Missing values
- Duplicates
- data type
- the number of unique values of each column
- statistics of data set
- various categories present in the different categorical column

## Exploratory Data Analysis (EDA)
- More Description can be found in the notebook folder

## Final Conclusions from EDA
- Student's Performance is related with lunch, race, parental level education
- Females lead in pass percentage and also are top-scorers
- Student's Performance is not much related with test preparation course
- Finishing preparation course is benefitial.

## Models used for Training
- Linear Regression
- Lasso
- Ridge
- K-Neighbours Regressor
- Decision Tree
- Random Forest Regressor
- XGB Regressor
- CatBoosting Regressor
- AdaBoost Regressor


## Run Locally in your computer

Clone the project

```bash
  git clone [https://github.com/VishweshJagadeesh/chennai-houseprice-predictor](https://github.com/VishweshJagadeesh/chennai-houseprice-predictor)
```

Go to the project directory

```bash
  cd my-project
```

After setting up environment and installing packages Run

```bash
  python application.py
```
then head on to your local host with port 8080 ie. `localhost:8080`


## Screenshots
![image](https://github.com/user-attachments/assets/60768e4e-b1a9-4c3f-a405-cf8fd4950ba2)
![image](https://github.com/user-attachments/assets/e4a77ced-18a2-4fc0-8b3e-82e29c17ced9)


