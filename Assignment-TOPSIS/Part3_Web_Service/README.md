# Part 3 — TOPSIS Web Service

This part implements a **Flask-based web application** for the TOPSIS package.

Users can upload a CSV file, enter weights and impacts, and receive the results.

---

## Features

* Upload CSV input file
* Enter weights and impacts
* Email input support
* Generates ranked output

---

## Project Structure

```
Part3_Web_Service
│
├── app.py
├── templates/
│   └── index.html
└── venv/
```

---

## Setup Instructions

### 1. Navigate to Part3 folder

```bash
cd Assignment-TOPSIS/Part3_Web_Service
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install flask pandas numpy
```

Install the TOPSIS package from Part2:

```bash
pip install -e ../Part2_PyPI_Package
```

---

### 4. Run the web server

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## How It Works

1. User uploads CSV file
2. Inputs weights and impacts
3. Submits form
4. TOPSIS is executed
5. Result file is generated

---

## Technologies Used

* Flask
* HTML
* Python
* NumPy
* Pandas
