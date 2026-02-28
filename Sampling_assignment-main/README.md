# Sampling Assignment — UCS654

**Assignment:** Sampling Techniques on Imbalanced Dataset

---

## Objective
To analyze how different sampling techniques affect the performance of machine learning models on an imbalanced dataset.

## Dataset Used
`Creditcard_data.csv`

## Steps Performed
1. Loaded dataset
2. Balanced dataset using SMOTE
3. Created 5 samples
4. Applied 5 sampling techniques
5. Trained 5 ML models
6. Compared accuracy

## Sampling Techniques Used
- Random Under Sampling
- Random Over Sampling
- SMOTE
- Tomek Links
- NearMiss

## Models Used
- Logistic Regression (M1)
- Decision Tree (M2)
- Random Forest (M3)
- SVM (M4)
- KNN (M5)

## Result Summary
Results are saved in `sampling_results.csv`

## Conclusion
The objective of this assignment was to analyze the effect of different sampling techniques on machine learning models when applied to an imbalanced dataset. From the experimental results, it is clear that sampling methods significantly influence model performance.

Among the five machine learning models tested, **Model M3 (Random Forest Classifier)** delivered the best performance, achieving 100% accuracy with Sampling1, and maintaining consistently high accuracy across all sampling techniques. This indicates that Random Forest is highly robust and well-suited for handling balanced as well as imbalanced datasets.

In terms of sampling techniques, **Sampling1** emerged as the most effective overall, providing the highest accuracy for three out of five models (M1, M3, and M4). However, the results also show that different models respond differently to sampling strategies — Sampling5 worked best for M2, while Sampling4 performed best for M5.

**Model M4 (SVM)** showed comparatively poor performance across all techniques, suggesting that it is more sensitive to class imbalance and sampling variations.

### Key Takeaways
- Random Forest is the most reliable model for this dataset
- Sampling1 is the most effective general-purpose sampling technique
- Choice of sampling technique should depend on the specific model being used

Selecting an appropriate combination of sampling technique and ML model is crucial for achieving optimal performance on imbalanced datasets.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
