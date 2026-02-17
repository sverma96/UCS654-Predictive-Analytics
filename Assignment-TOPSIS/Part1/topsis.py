import sys
import pandas as pd
import numpy as np


def topsis(input_file, weights, impacts, output_file):
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Error: Input file not found.")
        sys.exit(1)

    # Check minimum columns
    if data.shape[1] < 3:
        print("Error: Input file must contain at least three columns.")
        sys.exit(1)

    # Extract numeric data
    decision_matrix = data.iloc[:, 1:]

    # Check numeric values
    if not np.issubdtype(decision_matrix.dtypes.values[0], np.number):
        try:
            decision_matrix = decision_matrix.astype(float)
        except:
            print("Error: Non-numeric values found in decision matrix.")
            sys.exit(1)

    weights = weights.split(",")
    impacts = impacts.split(",")

    # Convert weights to float
    try:
        weights = np.array([float(w) for w in weights])
    except:
        print("Error: Weights must be numeric.")
        sys.exit(1)

    # Validate impacts
    if not all(i in ["+", "-"] for i in impacts):
        print("Error: Impacts must be '+' or '-'.")
        sys.exit(1)

    # Check length match
    if len(weights) != decision_matrix.shape[1] or len(impacts) != decision_matrix.shape[1]:
        print("Error: Number of weights, impacts, and columns must be same.")
        sys.exit(1)

    # Step 1: Normalize
    norm = decision_matrix / np.sqrt((decision_matrix ** 2).sum())

    # Step 2: Weighted matrix
    weighted = norm * weights

    # Step 3: Ideal best & worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Distance
    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Score
    score = dist_worst / (dist_best + dist_worst)

    # Ranking
    rank = score.rank(ascending=False)

    # Add to dataframe
    data["Topsis Score"] = score
    data["Rank"] = rank

    # Save output
    data.to_csv(output_file, index=False)
    print("Result saved to", output_file)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <input.csv> <weights> <impacts> <output.csv>")
        sys.exit(1)

    _, input_file, weights, impacts, output_file = sys.argv
    topsis(input_file, weights, impacts, output_file)

