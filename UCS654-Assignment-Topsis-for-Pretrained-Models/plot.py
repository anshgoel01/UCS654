import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("result.csv")

plt.bar(df["Model"], df["Score"])
plt.title("TOPSIS Ranking - Conversational Models")
plt.xlabel("Model")
plt.ylabel("Score")

plt.savefig("graph.png")
plt.show()