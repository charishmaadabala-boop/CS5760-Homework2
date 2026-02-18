# CS5760 Homework 2
# Q3 Bigram Probability and Smoothing
# Student Name: CHARISHMA ADABALA
# 700-700769626

bigram_counts = {
    ("<s>", "I"): 2,
    ("<s>", "deep"): 1,
    ("I", "love"): 2,
    ("love", "NLP"): 1,
    ("love", "deep"): 1,
    ("deep", "learning"): 2,
    ("learning", "</s>"): 1,
    ("learning", "is"): 1,
    ("NLP", "</s>"): 1,
    ("is", "fun"): 1,
    ("fun", "</s>"): 1,
    ("ate", "lunch"): 6,
    ("ate", "dinner"): 3,
    ("ate", "a"): 2,
    ("ate", "the"): 1
}

unigram_counts = {
    "<s>": 3,
    "I": 2,
    "love": 2,
    "deep": 2,
    "learning": 2,
    "NLP": 1,
    "ate": 12
}

def mle_prob(w1, w2):
    return bigram_counts.get((w1, w2), 0) / unigram_counts[w1]

print("P(I | <s>):", mle_prob("<s>", "I"))
print("P(love | I):", mle_prob("I", "love"))
print("P(NLP | love):", mle_prob("love", "NLP"))
print("P(noodle | ate):", mle_prob("ate", "noodle"))

# Laplace smoothing
def laplace_prob(w1, w2, V=10):
    return (bigram_counts.get((w1, w2), 0) + 1) / (unigram_counts[w1] + V)

print("Smoothed P(noodle | ate):", laplace_prob("ate", "noodle"))
