# CS5760 Homework 2
# Part II - Q1 Bigram Language Model
# Student Name: CHARISHMA ADABALA
# 700-700769626
from collections import defaultdict

corpus = [
    "<s> I love NLP </s>",
    "<s> I love deep learning </s>",
    "<s> deep learning is fun </s>"
]

unigram = defaultdict(int)
bigram = defaultdict(int)

for sentence in corpus:
    words = sentence.split()
    for i in range(len(words)):
        unigram[words[i]] += 1
        if i < len(words)-1:
            bigram[(words[i], words[i+1])] += 1

def bigram_probability(w1, w2):
    return bigram[(w1, w2)] / unigram[w1]

def sentence_probability(sentence):
    words = sentence.split()
    prob = 1
    for i in range(len(words)-1):
        prob *= bigram_probability(words[i], words[i+1])
    return prob

s1 = "<s> I love NLP </s>"
s2 = "<s> I love deep learning </s>"

p1 = sentence_probability(s1)
p2 = sentence_probability(s2)

print("Probability of S1:", p1)
print("Probability of S2:", p2)

if p1 > p2:
    print("Model prefers S1")
else:
    print("Model prefers S2")
