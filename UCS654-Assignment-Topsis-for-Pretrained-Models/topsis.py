import pandas as pd
import numpy as np

# STEP 1: Load data
df = pd.read_csv("data.csv")

print("Original Data:\n")
print(df)

# STEP 2: Create matrix (remove model names)
matrix = df.iloc[:,1:].values

# STEP 3: Normalization
norm = matrix / np.sqrt((matrix**2).sum(axis=0))

# STEP 4: Weights (simple equal weights)
weights = np.array([0.4,0.2,0.2,0.2])
weighted = norm * weights

# STEP 5: Impacts
impact = ["+","-","-","-"]

ideal_best = []
ideal_worst = []

for i in range(len(impact)):
    if impact[i] == "+":
        ideal_best.append(weighted[:,i].max())
        ideal_worst.append(weighted[:,i].min())
    else:
        ideal_best.append(weighted[:,i].min())
        ideal_worst.append(weighted[:,i].max())

ideal_best = np.array(ideal_best)
ideal_worst = np.array(ideal_worst)

# STEP 6: Distance calculation
dist_best = np.sqrt(((weighted - ideal_best)**2).sum(axis=1))
dist_worst = np.sqrt(((weighted - ideal_worst)**2).sum(axis=1))

# STEP 7: Score
score = dist_worst / (dist_best + dist_worst)

df["Score"] = score
df["Rank"] = df["Score"].rank(ascending=False)

# STEP 8: Save result
df.to_csv("result.csv", index=False)

print("\nFinal Result:\n")
print(df)