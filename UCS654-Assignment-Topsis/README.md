# Topsis Assignment - UCS654

This project implements the **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) method in three parts as required in the assignment.

---

## Part-I — Command Line Implementation

Command line implementation of TOPSIS. Takes a CSV file, weights and impacts, and generates a result file.

**Usage:**
```bash
python topsis.py input.csv "weights" "impacts" output.csv
```

**Example:**
```bash
python topsis.py input.csv "1,1,1,2" "+,+,-,+" result.csv
```

---

## Part-II — Python Package (PyPI)

Python package uploaded on PyPI.

- **Package Name:** `Topsis-Anshuman-102317042`
- **Install using:**
```bash
pip install Topsis-Anshuman-102317042
```
- **Run using:**
```bash
topsis input.csv "weights" "impacts" output.csv
```

---

## Part-III — Flask Web Service

Flask-based web service where the user uploads a file along with weights, impacts, and their email ID. The result CSV is sent to the provided email address.

**How to run:**
```bash
python app.py
```
Then open `http://localhost:5000` in your browser, upload your CSV, enter weights, impacts, and email — the result will be sent to your inbox.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Flask

---

## Author

**Anshuman Goel**
Roll Number: 102317042
UCS654 — Data Science
