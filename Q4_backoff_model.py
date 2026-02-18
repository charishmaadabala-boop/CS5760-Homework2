# CS5760 Homework 2
# Q4 Backoff Language Model
# Student Name: CHARISHMA ADABALA
# 700-700769626

from collections import defaultdict

# ---------------------------------------
# Training Corpus
# ---------------------------------------
corpus = [
    "<s> I like cats </s>",
    "<s> I like dogs </s>",
    "<s> You like cats </s>"
]

# ---------------------------------------
# Count bigrams and trigrams
# ---------------------------------------
bigram_counts = defaultdict(int)
trigram_counts = defaultdict(int)
unigram_counts = defaultdict(int)

for sentence in corpus:
    words = sentence.split()
    for i in range(len(words)):
        unigram_counts[words[i]] += 1
        if i < len(words)-1:
            bigram_counts[(words[i], words[i+1])] += 1
        if i < len(words)-2:
            trigram_counts[(words[i], words[i+1], words[i+2])] += 1

# ---------------------------------------
# Probability Functions
# ---------------------------------------
def trigram_prob(w1, w2, w3):
    return trigram_counts[(w1, w2, w3)] / bigram_counts[(w1, w2)]

def bigram_prob(w1, w2):
    return bigram_counts[(w1, w2)] / unigram_counts[w1]

# ---------------------------------------
# Q4.1 P(cats | I, like)
# ---------------------------------------
p_cats = trigram_prob("I", "like", "cats")

print("P(cats | I, like) =", p_cats)

# ---------------------------------------
# Q4.2 P(dogs | You, like) with backoff
# ---------------------------------------
if trigram_counts[("You", "like", "dogs")] > 0:
    p_dogs = trigram_prob("You", "like", "dogs")
    print("Using trigram probability.")
else:
    print("Trigram not found. Backing off to bigram.")
    p_dogs = bigram_prob("like", "dogs")

print("P(dogs | You, like) =", p_dogs)

# ---------------------------------------
# Q4.3 Explanation
# ---------------------------------------
print("\nWhy backoff is necessary:")
print("Some trigrams do not appear in the training data.")
print("Without backoff, their probability would be zero.")
print("Backoff allows us to use lower-order n-grams instead.")
