# Part 1 — Command Line TOPSIS

This part implements the **TOPSIS algorithm** as a command-line Python program.

---

## Usage

```bash
python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFileName>
```

### Example

```bash
python topsis.py data.csv "1,1,1,1" "+,+,-,+" result.csv
```

---

## Input Requirements

* Input file must be a **CSV file**
* Must contain **3 or more columns**
* First column: non-numeric (e.g., names)
* Remaining columns: numeric values

---

## Parameters

| Parameter      | Description                                     |
| -------------- | ----------------------------------------------- |
| InputDataFile  | CSV file containing alternatives and criteria   |
| Weights        | Comma-separated weights (e.g., `1,1,1,1`)       |
| Impacts        | `+` for benefit, `-` for cost (e.g., `+,+,-,+`) |
| OutputFileName | Output CSV with scores and ranks                |

---

## Output

The output CSV will contain:

* Original data
* TOPSIS Score
* Rank

Example:

| Fund | P1  | P2  | P3  | P4  | Score | Rank |
| ---- | --- | --- | --- | --- | ----- | ---- |
| M1   | ... | ... | ... | ... | 0.52  | 2    |

---

## How to Run

1. Open terminal in `Part1` folder.
2. Run:

```bash
python topsis.py data.csv "1,1,1,1" "+,+,-,+" result.csv
```

3. Check the generated `result.csv`.

---

## Files

```
Part1
│
├── topsis.py
├── data.csv
└── result.csv
```
