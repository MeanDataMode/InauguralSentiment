import random
import nltk
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *


# Import corpus (aka bank of inaugural speeches)
inaugural = nltk.corpus.inaugural.fileids()


# Set up dict to add sentiment to
pres = dict()


# Set up the Dictionary that will designate a word as positive or negative.
sentiment_scores = {}
with open("tidytext_sentiments.txt",'r') as infile :
    next(infile)
    for line in infile.readlines() :
        line = line.strip().split("\t")
        if line[1] == "positive" :
            sentiment_scores[line[0]] = 1
        else :
            sentiment_scores[line[0]] = -1


for file in inaugural:
    # open each speech
    
    # Assign the File name (without the ".txt") as the Dictonary Key
    key = str(file[:-4])
    
    # Assign the Speech Content to "the_words"
    the_words = nltk.corpus.inaugural.words(file)
    
    # create [*list=*] to save the sentiment analysis in
    scores = [0] * len(the_words)
    place = 0

    # Now its time to run the sentiment
    for idx, word in enumerate(the_words):
        if word in sentiment_scores:
            place += sentiment_scores[word.lower()]
        scores[idx] = place

    # Move Speech to Dictionary with
    pres[key]=scores

    
# write pres Dictionary to txt file
with open("inaugural_scores.txt", "w") as openfile:
    openfile.write("president\tword\tscore\n")
    for key in pres.keys():
        for idx, score in enumerate(pres[key]):
            openfile.write("\t".join([str(key),str(idx+1),str(score)]) + "\n")  

