import sys
import pandas as pd
import numpy as np


def topsis(input_file, weights, impacts, output_file):
    # Read input file
    data = pd.read_csv(input_file)

    # Check minimum columns
    if data.shape[1] < 3:
        raise ValueError("Input file must contain at least three columns")

    # Extract decision matrix (excluding first column)
    decision_matrix = data.iloc[:, 1:].values

    # Process weights and impacts
    weights = [float(w) for w in weights.split(",")]
    impacts = impacts.split(",")

    # Validate lengths
    if len(weights) != decision_matrix.shape[1]:
        raise ValueError("Number of weights must match number of columns")

    if len(impacts) != decision_matrix.shape[1]:
        raise ValueError("Number of impacts must match number of columns")

    for impact in impacts:
        if impact not in ["+", "-"]:
            raise ValueError("Impacts must be either '+' or '-'")

    # Step 1: Normalize decision matrix
    norm = decision_matrix / np.sqrt((decision_matrix ** 2).sum(axis=0))

    # Step 2: Apply weights
    weighted = norm * weights

    # Step 3: Determine ideal best and worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(max(weighted[:, i]))
            ideal_worst.append(min(weighted[:, i]))
        else:
            ideal_best.append(min(weighted[:, i]))
            ideal_worst.append(max(weighted[:, i]))

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Calculate distances
    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Calculate scores
    score = dist_worst / (dist_best + dist_worst)

    # Add results to dataframe
    data["Topsis Score"] = score
    data["Rank"] = data["Topsis Score"].rank(ascending=False, method="max")

    # Save output
    data.to_csv(output_file, index=False)


def main():
    if len(sys.argv) != 5:
        print("Usage: topsis input.csv weights impacts output.csv")
        sys.exit(1)

    _, input_file, weights, impacts, output_file = sys.argv
    topsis(input_file, weights, impacts, output_file)
