# CS5760 Homework 2
# Q5 Evaluation Metrics
# Student Name: CHARISHMA ADABALA
# 700-700769626

import numpy as np

# Confusion Matrix
# Rows = System Prediction
# Columns = Gold Labels
confusion_matrix = np.array([
    [5, 10, 5],
    [15, 20, 10],
    [0, 15, 10]
])

classes = ["Cat", "Dog", "Rabbit"]

print("Per-Class Precision and Recall\n")

precisions = []
recalls = []

for i, cls in enumerate(classes):
    TP = confusion_matrix[i][i]
    FP = sum(confusion_matrix[:, i]) - TP
    FN = sum(confusion_matrix[i]) - TP

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)

    precisions.append(precision)
    recalls.append(recall)

    print(cls)
    print(" Precision:", round(precision, 3))
    print(" Recall:", round(recall, 3))
    print()

# Macro averages
macro_precision = sum(precisions) / len(precisions)
macro_recall = sum(recalls) / len(recalls)

print("Macro-Averaged Precision:", round(macro_precision, 3))
print("Macro-Averaged Recall:", round(macro_recall, 3))

# Micro averages
TP_total = sum(confusion_matrix[i][i] for i in range(3))
total_samples = confusion_matrix.sum()

micro_precision = TP_total / total_samples
micro_recall = TP_total / total_samples

print("\nMicro-Averaged Precision:", round(micro_precision, 3))
print("Micro-Averaged Recall:", round(micro_recall, 3))
