# pre-processing

Data preprocessing is an essential step in building a Machine Learning model and depending on how well the data has been preprocessed; the results are seen.

In NLP, text preprocessing is the first step in the process of building a model.

The various text preprocessing steps are:

* Tokenization
* Lower casing
* Stop words removal
* Stemming
* Lemmatization

These various text preprocessing steps are widely used for dimensionality reduction.

In the vector space model, each word/term is an axis/dimension. The text/document is represented as a vector in the multi-dimensional space.
The number of unique words means the number of dimensions.

![image](https://user-images.githubusercontent.com/52862591/184932507-6c9a1a44-bdc3-4683-b765-ce007f5a2337.png)

Installation: The python library I’ll be using to implement the text preprocessing tasks is nltk

pip install nltk==3.4.5
Tokenization: Splitting the sentence into words.


Output: ['Books', 'are', 'on', 'the', 'table'] 
Lower casing: Converting a word to lower case (NLP -> nlp).
Words like Book and book mean the same but when not converted to the lower case those two are represented as two different words in the vector space model (resulting in more dimensions).


Output: books are on the table.
Stop words removal: Stop words are very commonly used words (a, an, the, etc.) in the documents. These words do not really signify any importance as they do not help in distinguishing two documents.


Output: ['Machine', 'Learning', 'cool', '!']
Explanation: Stop word ‘is’ has been removed
Stemming: It is a process of transforming a word to its root form.


Output: machin, learn, is, cool
Explanation: The word 'machine' has its suffix 'e' chopped off. The stem does not make sense as it is not a word in English. This is a disadvantage of stemming.
Lemmatization: Unlike stemming, lemmatization reduces the words to a word existing in the language.

Either Stemming or Lemmatization can be used. Libraries such as nltk, and spaCy have stemmers and lemmatizers implemented. These are built based on a rule-based approach.

Stemmer is easy to build than a lemmatizer as the latter requires deep linguistics knowledge in constructing dictionaries to look up the lemma of the word.

For lemmatization to resolve a word to its lemma, part of speech of the word is required. This helps in transforming the word into a proper root form. However, for doing so, it requires extra computational linguistics power such as a part of speech tagger.

Lemmatization is preferred over Stemming because lemmatization does a morphological analysis of the words.


Output: machine, care
Explanation: The word Machine transforms to lowercase and retains the same word unlike Stemming. Also, the word caring is transformed to its lemma 'care' as the parts of speech variable (pos) is verb(v)
In conclusion, these are the text preprocessing steps in NLP. Various python libraries like nltk, spaCy, and TextBlob can be used. Refer their documentation and try them out.

<a href="https://towardsdatascience.com/text-preprocessing-in-natural-language-processing-using-python-6113ff5decd8">Link to the article is here</a>