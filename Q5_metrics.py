# CS5760 Homework 2
# Q5 Confusion Matrix Metrics
# Student Name: CHARISHMA ADABALA
# 700-700769626

import numpy as np

confusion_matrix = np.array([
    [5, 10, 5],
    [15, 20, 10],
    [0, 15, 10]
])

classes = ["Cat", "Dog", "Rabbit"]

for i, cls in enumerate(classes):
    TP = confusion_matrix[i][i]
    FP = sum(confusion_matrix[:, i]) - TP
    FN = sum(confusion_matrix[i]) - TP

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)

    print(cls)
    print(" Precision:", round(precision, 3))
    print(" Recall:", round(recall, 3))
    print()

# Macro average
precisions = []
recalls = []

for i in range(3):
    TP = confusion_matrix[i][i]
    FP = sum(confusion_matrix[:, i]) - TP
    FN = sum(confusion_matrix[i]) - TP
    precisions.append(TP/(TP+FP))
    recalls.append(TP/(TP+FN))

print("Macro Precision:", sum(precisions)/3)
print("Macro Recall:", sum(recalls)/3)

# Micro average
TP_total = sum(confusion_matrix[i][i] for i in range(3))
Total = confusion_matrix.sum()

print("Micro Precision:", TP_total/Total)
print("Micro Recall:", TP_total/Total)
