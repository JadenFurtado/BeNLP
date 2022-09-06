
"""
TO DO:
●	Convert number words to numeric form
●	Remove numbers
●	Phrase extraction
●	Script Validation
"""
import re
import nltk
import pke
from nltk.tokenize import sent_tokenize
import contractions
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from word2number import w2n

# silly test html
raw_html = """<a href='#'>hi</a>            <b>.hello</b>. This is us. You'll. One million"""
cleantext = BeautifulSoup(raw_html, "lxml").text

def removeWhiteSpaces(sentence):
    sentence = " ".join(re.split("\s+", sentence, flags=re.UNICODE))
    return sentence


def getSentences(text):
    return sent_tokenize(text)

def removeContractions(text):
    newText = list()
    for sentece in text:
        newText.append(contractions.fix(sentece))
    return newText

def removeSpecialChars(text):
    newText = list()
    for sentence in text:
        newText.append(re.sub('[^A-Za-z0-9]+', ' ', sentence))
    return newText
def toLowerCase(text):
    newText = list()
    for sentence in text:
        newText.append(sentence.lower())
    return newText

def textTokenize(text):
    newList = list()
    for sentence in text:
        newList.append(word_tokenize(sentence))
    return newList


def keyPhraseExtraction(cleantext):
    # initialize keyphrase extraction model, here TopicRank
    extractor = pke.unsupervised.TopicRank()
    extractor.load_document(
        cleantext,
        language='en',
        normalization='stemming')

    # select the keyphrase candidates, for TopicRank the longest sequences of 
    # nouns and adjectives
    extractor.candidate_selection(pos={'NOUN', 'PROPN', 'ADJ'})

    # weight the candidates using a random walk. The threshold parameter sets the
    # minimum similarity for clustering, and the method parameter defines the 
    # linkage method
    extractor.candidate_weighting(threshold=0.74,
                                method='average')
    keyPhraseList = list()
    # print the n-highest (10) scored candidates
    for (keyphrase, score) in extractor.get_n_best(n=1, stemming=True):
        print(keyphrase, score)
        keyPhraseList.append([keyphrase,score])
    return keyPhraseList
    

def convertToNumbers(text):
    newText = list()
    for test_str in text:
        # Convert numeric words to numbers
        # Using word2number
        try:
            res = w2n.word_to_num(test_str)
        except:
            res = test_str
        newText.append(str(res))
    return newText

def removeNumbers(text):
    newText = list()
    for ini_string in text:
        # using join and isdigit
        # to remove numeric digits from string
        res = ''.join([i for i in ini_string if not i.isdigit()])
        newText.append(res)
    return newText

# initializing string
text = removeWhiteSpaces(cleantext)
text = getSentences(text)
text = removeContractions(text)
text = removeSpecialChars(text)
text = toLowerCase(text)
text = convertToNumbers(text)
text = removeNumbers(text)
text = textTokenize(text)
listOfKeyPhrases = keyPhraseExtraction(cleantext)