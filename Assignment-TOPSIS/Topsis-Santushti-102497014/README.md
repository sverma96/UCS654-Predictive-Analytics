# Topsis-Santushti-102497014

A Python package that implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method for multi-criteria decision making.

---

## Installation

Install the package using pip:

```bash
pip install Topsis-Santushti-102497014
```

---

## Usage

Run the package from the command line:

```bash
topsis input.csv "1,1,1,1" "+,+,-,+" output.csv
```

### Arguments

1. **input.csv**
   Input CSV file containing alternatives and criteria values.

2. **weights**
   Comma-separated weights for each criterion.
   Example:

   ```bash
   "1,1,1,1"
   ```

3. **impacts**
   Comma-separated impacts for each criterion.
   Use:

   * `+` for beneficial criteria
   * `-` for non-beneficial criteria

   Example:

   ```bash
   "+,+,-,+"
   ```

4. **output.csv**
   Output file that will contain:

   * Topsis Score
   * Rank

---

## Output

The output file will include:

* Original data
* Topsis Score
* Rank of each alternative

---

## Example

```bash
topsis data.csv "1,2,3,4" "+,+,-,+" result.csv
```

This command will generate `result.csv` containing the TOPSIS scores and rankings.

