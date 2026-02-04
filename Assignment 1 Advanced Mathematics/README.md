# Assignment 1 – Advanced Mathematics

## Title

**Learning Probability Density Functions using Roll-Number-Parameterized Non-Linear Model**

---

## 1. Introduction

This assignment focuses on learning a probability density function (PDF) from real-world air quality data using a roll-number-parameterized non-linear transformation. The objective is to understand data transformation, parameter estimation, and probabilistic modeling using mathematical and statistical concepts.

The NO₂ (Nitrogen Dioxide) feature from the *India Air Quality Dataset* is used to demonstrate how non-linear transformations affect data distribution and how a suitable probability density function can be learned from the transformed data.

---

## 2. Dataset Description

* **Dataset Name:** India Air Quality Data
* **Source:** Kaggle
* **Feature Used:** NO₂ concentration
* **Data Type:** Continuous numerical values

Before processing, missing values are removed to ensure accurate statistical estimation.

---

## 3. Methodology

The overall workflow followed in this assignment is shown below:

**Data Loading → Data Cleaning → Non-Linear Transformation → PDF Parameter Estimation → Result Visualization**

### 3.1 Data Loading and Pre-processing

* Dataset loaded using Pandas
* NO₂ feature extracted
* Missing values removed

### 3.2 Non-Linear Transformation (Step 1)

Each value of the feature (x) is transformed into (z) using the roll-number-based transformation:


<img width="766" height="291" alt="image" src="https://github.com/user-attachments/assets/67a5bf69-97f7-45ab-9004-616499c99405" />



## 4. Probability Density Function Learning (Step 2)

The transformed variable (z) is modeled using the following probability density function:

<img width="292" height="57" alt="image" src="https://github.com/user-attachments/assets/88edce0d-dd09-4520-b19c-df0d0f8c0443" />



### Parameter Estimation

* **Mean (μ)** 
* **Variance (σ²)**
* **Lambda (λ)**
* **Normalization Constant (c)** 

These parameters are computed directly from the transformed data.

---

## 5. Results and Analysis

### 5.1 Estimated Parameters

The learned parameters of the probability density function are:

* **μ (Mean):** Computed from transformed data
* **λ (Lambda):** Controls the spread of the distribution
* **c (Normalization Constant):** Ensures valid probability density


---

## 6. Result Visualization

* Histogram of transformed variable (z)
* Learned probability density function plotted over the histogram

This visualization shows that the learned PDF closely follows the empirical distribution of the transformed data.

---

## 7. Implementation Details

* **Language:** Python
* **Libraries Used:** NumPy, Pandas, Matplotlib
* **Platform:** Jupyter Notebook / Google Colab

---
## 8. Live Link 
https://colab.research.google.com/drive/1LJY8M6tp7GWqth4etxGi_ghE8BxfCrdK

## 9. Screenshot of the Interface 

<img width="1763" height="813" alt="image" src="https://github.com/user-attachments/assets/1131ce26-ca53-4c0a-9a47-eefc14f26dca" />

