# CS5760 Homework 2
Part I – Q5 Evaluation Metrics from Confusion Matrix
Student Name: CHARISHMA ADABALA
700-769626

Confusion Matrix

            Gold
System     Cat   Dog   Rabbit
Cat         5    10      5
Dog        15    20     10
Rabbit      0    15     10

---

## Per-Class Metrics

Cat:
TP = 5  
FP = 15 + 0 = 15  
FN = 10 + 5 = 15  

Precision = TP / (TP + FP) = 5 / (5 + 15) = 0.25  
Recall = TP / (TP + FN) = 5 / (5 + 15) = 0.25  

---

Dog:
TP = 20  
FP = 10 + 15 = 25  
FN = 15 + 10 = 25  

Precision = 20 / (20 + 25) = 0.44  
Recall = 20 / (20 + 25) = 0.44  

---

Rabbit:
TP = 10  
FP = 5 + 10 = 15  
FN = 0 + 15 = 15  

Precision = 10 / (10 + 15) = 0.40  
Recall = 10 / (10 + 15) = 0.40  

---

## Macro-Averaged Metrics

Macro Precision  
= (0.25 + 0.44 + 0.40) / 3  
= 0.36  

Macro Recall  
= (0.25 + 0.44 + 0.40) / 3  
= 0.36  

---

## Micro-Averaged Metrics

Total True Positives  
= 5 + 20 + 10 = 35  

Total Samples  
= 90  

Micro Precision = 35 / 90 = 0.39  
Micro Recall = 35 / 90 = 0.39  

---

## Interpretation

Macro-averaging treats all classes equally.  
Micro-averaging gives more weight to larger classes.
