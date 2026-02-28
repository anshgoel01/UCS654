import sys
import pandas as pd
import numpy as np

if len(sys.argv) != 5:
    print("Error: Incorrect number of parameters.")
    sys.exit(1)

input_file = sys.argv[1]
weights = sys.argv[2]
impacts = sys.argv[3]
output_file = sys.argv[4]

try:
    data = pd.read_csv(input_file)
except:
    print("Error: File not found.")
    sys.exit(1)

if data.shape[1] < 3:
    print("Error: Input file must contain at least 3 columns.")
    sys.exit(1)

weights = weights.split(',')
impacts = impacts.split(',')

for col in data.columns[1:]:
    if not pd.api.types.is_numeric_dtype(data[col]):
        print("Error: Non numeric values found.")
        sys.exit(1)

if len(weights) != len(data.columns)-1 or len(impacts) != len(weights):
    print("Error: Weights, impacts and columns mismatch.")
    sys.exit(1)

for i in impacts:
    if i not in ['+','-']:
        print("Error: Impacts must be + or - only.")
        sys.exit(1)

weights = [float(w) for w in weights]

matrix = data.iloc[:,1:].values

norm = np.sqrt((matrix**2).sum(axis=0))
norm_matrix = matrix / norm

weighted = norm_matrix * weights

ideal_best = []
ideal_worst = []        

for i in range(len(impacts)):
    if impacts[i] == '+':
        ideal_best.append(weighted[:,i].max())
        ideal_worst.append(weighted[:,i].min())
    else:
        ideal_best.append(weighted[:,i].min())
        ideal_worst.append(weighted[:,i].max())

ideal_best = np.array(ideal_best)
ideal_worst = np.array(ideal_worst)

dist_best = np.sqrt(((weighted - ideal_best)**2).sum(axis=1))
dist_worst = np.sqrt(((weighted - ideal_worst)**2).sum(axis=1))

score = dist_worst / (dist_best + dist_worst)

data['Topsis Score'] = score
data['Rank'] = data['Topsis Score'].rank(method='max', ascending=False).astype(int)

data.to_csv(output_file, index=False)

print("Success: Result saved to", output_file)
