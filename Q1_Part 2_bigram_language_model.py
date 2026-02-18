# CS5760 Homework 2
# Part II - Q1 Bigram Language Model
# Student Name: CHARISHMA ADABALA
# 700-700769626

from collections import defaultdict

# Training corpus
corpus = [
    "<s> I love NLP </s>",
    "<s> I love deep learning </s>",
    "<s> deep learning is fun </s>"
]

unigram_counts = defaultdict(int)
bigram_counts = defaultdict(int)

# Count unigrams and bigrams
for sentence in corpus:
    words = sentence.split()
    for i in range(len(words)):
        unigram_counts[words[i]] += 1
        if i < len(words) - 1:
            bigram_counts[(words[i], words[i+1])] += 1

# Compute bigram probability using MLE
def bigram_prob(w1, w2):
    return bigram_counts[(w1, w2)] / unigram_counts[w1]

# Compute sentence probability
def sentence_probability(sentence):
    words = sentence.split()
    prob = 1
    for i in range(len(words)-1):
        prob *= bigram_prob(words[i], words[i+1])
    return prob

s1 = "<s> I love NLP </s>"
s2 = "<s> I love deep learning </s>"

p1 = sentence_probability(s1)
p2 = sentence_probability(s2)

print("Sentence 1 Probability:", p1)
print("Sentence 2 Probability:", p2)

if p1 > p2:
    print("Model prefers: Sentence 1")
else:
    print("Model prefers: Sentence 2")
