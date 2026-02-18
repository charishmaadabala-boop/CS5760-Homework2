# CS5760 Homework 2
# Part I – Q1 Worked Example: Document Classification  
# Student Name: CHARISHMA ADABALA
# 700-769626

---

## Test Document
"predictable no fun"

---

## Given Priors

P(Positive) = 0.5  
P(Negative) = 0.5  

---

## Smoothed Word Likelihoods

predictable  
P(predictable | Positive) = 0.01  
P(predictable | Negative) = 0.05  

no  
P(no | Positive) = 0.02  
P(no | Negative) = 0.06  

fun  
P(fun | Positive) = 0.08  
P(fun | Negative) = 0.01  

---

## Positive Class Calculation

P(Positive | d)  
= P(Positive) × P(predictable | Positive) × P(no | Positive) × P(fun | Positive)

= 0.5 × 0.01 × 0.02 × 0.08  

= 0.5 × 0.000016  

= 0.000008  

---

## Negative Class Calculation

P(Negative | d)  
= P(Negative) × P(predictable | Negative) × P(no | Negative) × P(fun | Negative)

= 0.5 × 0.05 × 0.06 × 0.01  

= 0.5 × 0.00003  

= 0.000015  

---

## Final Decision

Since 0.000015 > 0.000008,  
the document is classified as NEGATIVE.
