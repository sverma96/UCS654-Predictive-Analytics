# Data Generation using Modelling and Simulation for Machine Learning

## Project Overview

This project demonstrates synthetic data generation using mathematical modelling and simulation, followed by predictive modelling using multiple Machine Learning regression algorithms.

An epidemiological SIR (Susceptible–Infected–Recovered) model is implemented to simulate the spread of an infectious disease under varying parameter conditions. The generated synthetic dataset is then used to train and evaluate regression models to predict the Peak Infected Population.

---

## Objective

- Generate synthetic epidemic data using simulation.
- Define and analyze important model parameters.
- Perform 1000 simulation runs.
- Train and compare multiple regression models.
- Identify the best-performing predictive model.

---

## Simulation Model – SIR Model

The SIR model divides the total population into three compartments:

- S – Susceptible  
- I – Infected  
- R – Recovered  

The governing differential equations are:

dS/dt = -β(SI/N)  
dI/dt = β(SI/N) - γI  
dR/dt = γI  

Where:

- β (Beta) = Infection Rate  
- γ (Gamma) = Recovery Rate  
- N = Total Population  

The target variable for prediction is:

Peak Infected Population

---

## Parameter Bounds Used in Simulation

| Parameter         | Description               | Lower Bound | Upper Bound |
|------------------|--------------------------|------------|------------|
| Beta             | Infection Rate           | 0.1        | 1.0        |
| Gamma            | Recovery Rate            | 0.05       | 0.5        |
| Initial_Infected | Initial infected count   | 1          | 50         |
| Population       | Total population         | 500        | 2000       |
| Days             | Simulation duration      | 50         | 200        |

---

## Data Generation Process

- 1000 simulations were performed.
- Parameters were randomly sampled within defined bounds.
- For each simulation, the Peak Infected value was recorded.
- The final dataset contains 1000 rows.

Dataset file:

`generated_dataset.csv`

---

## Machine Learning Models Used

The following regression models were trained and evaluated:

1. Linear Regression  
2. Ridge Regression  
3. Decision Tree Regressor  
4. Random Forest Regressor  
5. Gradient Boosting Regressor  
6. Support Vector Regressor (SVR)  
7. K-Nearest Neighbors (KNN)

---

## Data Preprocessing

Feature scaling using StandardScaler was applied to:

- Linear Regression
- Ridge Regression
- SVR
- KNN

Tree-based models were trained on original features since they are scale-invariant.

---

## Evaluation Metrics

Models were evaluated using:

- R² Score
- Mean Squared Error (MSE)

---

## Results Summary

| Model              | R² Score |
|--------------------|----------|
| Gradient Boosting  | 0.983    |
| Random Forest      | 0.982    |
| Decision Tree      | 0.946    |
| KNN                | 0.937    |
| Linear Regression  | 0.822    |
| Ridge Regression   | 0.822    |
| SVR                | 0.119    |

Gradient Boosting achieved the highest predictive accuracy.

---

## Feature Importance Analysis

The Gradient Boosting model identified the following importance ranking:

1. Gamma (Recovery Rate)
2. Beta (Infection Rate)
3. Population
4. Initial_Infected
5. Days

This aligns with epidemiological theory, as epidemic growth is primarily governed by transmission and recovery dynamics.

---

## Project Structure

Data Generation using Modelling and Simulation for ML/

├── SIR_Simulation.ipynb  
├── generated_dataset.csv  
├── README.md  

---

## Conclusion

This project successfully demonstrates how modelling and simulation can be used to generate synthetic datasets for machine learning applications.

Among all evaluated models, Gradient Boosting achieved the highest R² score, indicating superior predictive capability for nonlinear epidemic dynamics.

The study highlights the effectiveness of simulation-based synthetic data in predictive analytics and decision-support modelling.

---

## Technologies Used

- Python 3.11
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- VS Code
- Git and GitHub