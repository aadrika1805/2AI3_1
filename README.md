Project Title
Insurance Cost Prediction using Linear Regression

Team Members<br>
<li>
<ul>AADRIKA JHA(Team Lead)<br></ul>
<ul>ABHASH SHARMA<br></ul>
<ul>ALISA SAHOO<br></ul>
<ul>AMARDIP KUMAR<br></ul>
<ul>BELIM FAISALKHAN ANWARKHAN<br></ul>
<ul>CHOVATIYA VRAJ HITESHBHAI<br></ul>
</li>

<hr>
<b>Problem Statement<b>

The objective of this project is to build a Machine Learning model that predicts medical insurance charges based on various input features such as age, gender, BMI, number of children, smoking habits, and region.
<hr>

Dataset Description

We used the Medical Cost Personal Dataset.

Features:
<hr>

age: Age of the individual
sex: Gender (male/female)
bmi: Body Mass Index
children: Number of dependents
smoker: Smoking status (yes/no)
region: Residential area
<hr>

Target:

charges: Medical insurance cost
 Data Preprocessing Steps
Loaded dataset using pandas
Checked for missing values
Converted categorical data:
sex → numerical
smoker → numerical
Applied one-hot encoding for region
Prepared dataset for model training
 Model Used and Training Details
Model: Linear Regression
Split data into training and testing sets (80/20)
Trained model using sklearn
Generated predictions on test data
<hr>

Model Evaluation Results
 
Mean Absolute Error (MAE) calculated
R² Score used to evaluate model performance
Model showed good prediction capability for insurance charges
 <hr>

GitHub Collaboration Summary

Repository was created by team lead
Team members worked on separate branches
Tasks were divided (preprocessing, encoding, model, etc.)
Pull requests were created and merged into main branch
Final integration done in main notebook
<hr>

Conclusion

This project successfully demonstrates the use of Machine Learning for predicting insurance costs. It helped in understanding data preprocessing, model training, evaluation, and collaborative development using GitHub.
