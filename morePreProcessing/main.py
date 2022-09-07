#3.	Apply various other text pre-processing techniques for any given text : Stop Word  Removal, Lemmatization / Stemming
from os import remove
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer 
ps = PorterStemmer()

sentence = "Books are on the table"

# tokenization
words = word_tokenize(sentence)

def removeStopWords(text):
    stop_words = set(stopwords.words('english')) 
    newSentences = list()
    for sentence in text:
        word_tokens = word_tokenize(sentence)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        newSentences.append(filtered_sentence) 
    return newSentences

# stemming
def stemmingWords(sentence):
    stemmedWords = list()
    for word in sentence.split():
        stemmedWords.append(ps.stem(word))
    return stemmedWords

# Lemmatization:
def lemmatizeWords(words):
    lemmatizer = WordNetLemmatizer()
    newWords = list()
    for word in words:
        wordNoun = lemmatizer.lemmatize("Machine", pos='n')
        # pos: parts of speech tag, verb
        wordVerb = lemmatizer.lemmatize("caring", pos='v')
        newWords.append([wordNoun,wordVerb])
    return newWords

print("Before pre processing:"+sentence)
print("After removal of stop-words:"+str(removeStopWords([sentence])))
print("After stemming:"+str(stemmingWords(sentence)))
print("After lemmatization:"+str(lemmatizeWords(words)))