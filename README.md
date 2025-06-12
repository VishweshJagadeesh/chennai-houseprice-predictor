
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
- Deployment using ECR and EC2 instances(CI/CD) to [this repository](https://github.com/VishweshJagadeesh/chennai-deployment) using AWS

## Dataset
- Dataset Source - [https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977](https://www.kaggle.com/datasets/kunwarakash/chennai-housing-sales-price)
- the dataset contains 22 columns and 7109 rows

## Dataset information
- PRT_ID:        Unique property identifier
- AREA:          Location/area of the property
- INT_SQFT:      Interior square footage of the property
- DATE_SALE:     Date of sale
- DIST_MAINROAD: Distance from main road
- N_BEDROOM:     Number of bedrooms
- N_BATHROOM:    Number of bathrooms
- N_ROOM:        Number of rooms
- SALE_COND:     Sale condition
- PARK_FACIL:    Parking facility
- DATE_BUILD:    Year of construction
- BUILDTYPE:     Type of building
- UTILITY_AVAIL: Utilities available
- STREET:        Street type
- MZZONE:        Market zone
- QS_ROOMS:      Quality of rooms
- QS_BATHROOM:   Quality of bathrooms
- QS_BEDROOM:    Quality of bedrooms
- QS_OVERALL:    Overall quality
- REG_FEE:       Registration fee
- COMMIS:        Commission
- SALES_PRICE:   Sale price of the property

## Data Checks Performed
- Missing values
- Duplicates
- data type
- the number of unique values of each column
- statistics of data set
- various categories present in the different categorical column

## Exploratory Data Analysis (EDA)
- More Description can be found in the notebook folder

## Models used for Training
The machine learning model used for house price prediction is trained on the dataset using regression algorithms such as Linear Regression, Random Forest Regression, and Gradient Boosting Regression. The model is evaluated based on various metrics such as Mean Absolute Error, Mean Squared Error, and R-squared value to ensure its accuracy and performance.


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
