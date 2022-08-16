from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer 
ps = PorterStemmer()

sentence = "Books are on the table"

# tokenization
words = word_tokenize(sentence)
print("post tokenization:")
print(words)
"""
# you can also use split() to convert the sentence into word list
word = sentence.split()
print(word)
"""
# lower case:
sentence = sentence.lower()
print("to lower case:")
print(sentence)

# stop word removal
stop_words = set(stopwords.words('english')) 
word_tokens = word_tokenize(sentence)
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
print("after stop words are removed")
print(filtered_sentence)

# stemming
print("after stemming")
for word in sentence.split():
  print(ps.stem(word))

# Lemmatization:
lemmatizer = WordNetLemmatizer()
# example for reference
print("after lemmatization")
print(lemmatizer.lemmatize("Machine", pos='n'))
# pos: parts of speech tag, verb
print(lemmatizer.lemmatize("caring", pos='v'))