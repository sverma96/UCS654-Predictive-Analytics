# TOPSIS Assignment

This repository contains the implementation of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method in three stages as part of the coursework.

## Repository Structure

```
Assignment-TOPSIS
│
├── Part1
│   ├── topsis.py
│   ├── data.csv
│   └── result.csv
│
├── Part2_PyPI_Package
│   ├── topsis/
│   ├── pyproject.toml
│   ├── setup.cfg
│   └── README.md
│
└── Part3_Web_Service
    ├── app.py
    ├── templates/
    │   └── index.html
    └── README.md
```

---

## Description of Each Part

### Part 1 — Command Line TOPSIS

Implements the TOPSIS algorithm as a **command-line Python program**.
The program takes an input CSV file, weights, and impacts, and produces a ranked output file.

---

### Part 2 — Python Package (PyPI style)

Converts the TOPSIS implementation into a **proper Python package**.
The package can be installed and reused like any other Python library.

---

### Part 3 — Web Service

Creates a **Flask-based web interface** for the TOPSIS package where users can:

* Upload input CSV
* Provide weights and impacts
* Enter email
* Receive results

---

## Technologies Used

* Python
* NumPy
* Pandas
* Flask
* PyPI packaging tools

---

## Objective

The assignment demonstrates:

* Algorithm implementation
* Command-line interface design
* Python packaging
* Web service development
