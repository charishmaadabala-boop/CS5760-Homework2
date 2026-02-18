# CS5760-Homework2
Homework 2 - Natural Language Processing– Spring 2026
Student Name: CHARISHMA ADABALA 
University of Central Missouri 
700-700769626

## Repository Contents

Q1_bigram_language_model.py  
Implements a Bigram Language Model using Maximum Likelihood Estimation (MLE).  
Computes unigram and bigram counts, estimates probabilities, and compares sentence probabilities.

Q3_bigram_math.py  
Computes bigram probabilities, demonstrates the zero-probability problem, and applies Laplace (Add-1) smoothing.

Q5_metrics.py  
Computes precision, recall, macro-averaged, and micro-averaged metrics from a confusion matrix.

---

## How to Run Programs

1. Install Python
2. Open terminal or command prompt
3. Navigate to this repository folder
4. Run any file:

python filename.py

Example:
python Q1_bigram_language_model.py

---

## Part I – Written Answers

---

### Q1. Worked Example: Document Classification

Test document: "predictable no fun"

Assume:
P(positive) = 0.5  
P(negative) = 0.5  

Word likelihoods:

predictable  
P(word|pos) = 0.01  
P(word|neg) = 0.05  

no  
P(word|pos) = 0.02  
P(word|neg) = 0.06  

fun  
P(word|pos) = 0.08  
P(word|neg) = 0.01  

Positive score:

P(pos|d) = 0.5 × 0.01 × 0.02 × 0.08  
= 0.000008  

Negative score:

P(neg|d) = 0.5 × 0.05 × 0.06 × 0.01  
= 0.000015  

Decision:  
Since negative score > positive score, the document is classified as NEGATIVE.

---

### Q2. Harms of Classification

1. Representational Harm

Representational harm occurs when a classification system reinforces harmful stereotypes or biased representations of social groups.

Kiritchenko & Mohammad (2018) showed that sentiment lexicons often associate words related to women and minority groups with more negative sentiment, leading to biased predictions.

2. Risk of Censorship in Toxicity Classification

Toxicity classifiers may incorrectly label non-toxic language from marginalized communities as toxic, leading to over-censorship and silencing of those users.

3. Why Performance is Worse on African American English or Indian English

Most training data is dominated by Standard American English, so dialectal varieties are underrepresented and models fail to learn their patterns.

---

### Q3. Bigram Probabilities and Zero Probability

Sentence S1: <s> I love NLP </s>  

P(S1) = P(I|<s>) × P(love|I) × P(NLP|love) × P(</s>|NLP)  
= (2/3) × 1 × (1/2) × 1  
= 1/3  

Sentence S2: <s> I love deep learning </s>  

P(S2) = (2/3) × 1 × (1/2) × 1 × (1/2)  
= 1/6  

More probable sentence: S1

Zero-probability example:

P(noodle|ate) = 0/12 = 0  

This causes the entire sentence probability to become zero.

Laplace smoothing:

P(noodle|ate) = (0+1)/(12+10) = 1/22

---

### Q4. Backoff Model

Training sentences:

<s> I like cats </s>  
<s> I like dogs </s>  
<s> You like cats </s>  

P(cats | I, like) = 1/2  

P(dogs | You, like) → trigram not found  
Back off to bigram:

P(dogs | like) = 1/3  

Backoff is necessary because many trigrams do not appear in small training corpora and would otherwise have zero probability.

---

### Q5. Evaluation Metrics

Confusion Matrix:

Cat Dog Rabbit  
Cat     5   10   5  
Dog    15   20  10  
Rabbit  0   15  10  

Per-class metrics:

Cat  
Precision = 5 / (5+15+0) = 0.25  
Recall = 5 / (5+10+5) = 0.25  

Dog  
Precision = 20 / (10+20+15) = 0.44  
Recall = 20 / (15+20+10) = 0.44  

Rabbit  
Precision = 10 / (5+10+10) = 0.40  
Recall = 10 / (0+15+10) = 0.40  

Macro-averaged Precision = 0.36  
Macro-averaged Recall = 0.36  

Micro-averaged Precision = 35/90 = 0.39  
Micro-averaged Recall = 35/90 = 0.39  

## Interpretation

Macro-averaging treats each class equally, regardless of how many examples it has.  
Micro-averaging gives more importance to classes with more examples.

---

## Programming Implementation

The Python file `Q5_metrics.py`:

- Accepts the confusion matrix as input  
- Computes per-class precision and recall  
- Computes macro-averaged precision and recall  
- Computes micro-averaged precision and recall  
- Prints all results clearly  

To run:

python Q5_metrics.py


## Part II – Programming

See Python files in this repository:

Q1_bigram_language_model.py  
Q3_bigram_math.py  
Q5_metrics.py  

Each file is commented and prints outputs directly.
---


### Q1. Bigram Language Model Implementation

File: Q1_bigram_language_model.py

This program satisfies the required tasks as follows:

1. Reads the training corpus:
   <s> I love NLP </s>  
   <s> I love deep learning </s>  
   <s> deep learning is fun </s>

2. Computes unigram counts.

3. Computes bigram counts.

4. Estimates bigram probabilities using Maximum Likelihood Estimation (MLE).

5. Implements a function that computes the probability of any sentence.

6. Tests the function on:
   <s> I love NLP </s>  
   <s> I love deep learning </s>

7. Prints both sentence probabilities.

8. Prints which sentence the model prefers.

9. Explains preference based on higher probability.

Additional programs:

Q3_bigram_math.py – Bigram probabilities and Laplace smoothing  
Q5_metrics.py – Precision, recall, macro and micro averaging




