Tokenization using spaCy
========================
[![Built with spaCy](https://img.shields.io/badge/made%20with%20❤%20and-spaCy-09a3d5.svg)](https://spacy.io)

[spaCy](https://github.com/explosion/spaCy) is a library for advanced Natural Language Processing in Python and Cython. It's built on the very latest research, and was designed from day one to be used in real products. (Source: [spaCy](https://github.com/explosion/spaCy))

Introduction
------------
Tokenizer is a tool that splits a given text into tokens using regular expressions. The process of tokenizing a text into segments of words and punctuation in Spacy is done in several processes. It reads text from left to right. To begin, the tokenizer separated the text on whitespace in the same way that the split() method does. The tokenizer then checks to see whether the substring fits the tokenizer exception rules.

## ⏳ Install spaCy

For detailed installation instructions and other operating system, can be refer
[here](https://spacy.io/usage).

- **Operating system**: macOS / OS X · Linux · Windows (Cygwin, MinGW, Visual
  Studio)
- **Python version**: Python 3.6+ (only 64 bit)
- **Package managers**: [pip] · [conda] (via `conda-forge`)

[pip]: https://pypi.org/project/spacy/
[conda]: https://anaconda.org/conda-forge/spacy

Installation for macOS (my operating system):

```
# Download best-matching version of specific model for your spaCy installation
python -m spacy download en_core_web_sm

pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
```
## 📦 Loading & Using Models
To load a model, use [`spacy.load()`](https://spacy.io/api/top-level#spacy.load)
with the model name or a path to the model data directory.

```python
import glob
import spacy

nlp = spacy.load(name='en_core_web_sm')
```

Define your local path where you put the text files.
```python
path = '/Users/risehill/Documents/09-NLPProcessing/TextExtracted/steeples1998.txt'
```
## 👾 Let's get through the Codes!
```python
for file in glob.glob(path):
    with open(file, encoding='utf-8', errors='ignore') as file_in:
        text = file_in.read()
```
In this line of code, the text in paragraph converted into one string everytime it is found any new line
```python
# Replace the newline as one string
 Newtext = text.replace('\n', ' ')
# Check number of text contents in original Text files
 print(len(Newtext))
```

Check the tokenisation details:
```python
text_cleans.append(CleanText)
        print('-----------------------------------------------------------------------------------------------------------')
        print('CHECK TOKENISATION DETAILS')
        print('-----------------------------------------------------------------------------------------------------------')
        # Checking the details of the tokens
        for line in lines:
            line = nlp(line)
            for token in TextCleaned:
                my_doc_cleaned = [token for token in line if not token.is_stop and not token.is_punct and not token.is_space]
                analyzeToken ='{:<5}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(token.i, token.idx, token.text_with_ws, token.is_space, token.is_punct, token.is_stop,)
                analyzeToken2 = '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(token.i, token.text, token.is_alpha, token.shape_,  token.is_ascii, token.is_digit)
                analyzeToken3 = '{:<5}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(token.i, token.text, token.like_num,
                                                                                   token.like_url, token.like_email,
                                                                                   token.is_ascii, token.is_digit)
                analyzeToken4 = '{:<5}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(token.i, token.text, token.is_left_punct,
                                                                                   token.is_right_punct, token.is_bracket,
                                                                                   token.is_quote, token.is_currency)
                analyzeToken5 = '{:<15}{:<15}{:<15}'.format(token.i, token.text, token.text.istitle())
                print(analyzeToken)
```

The program output will be like this:

    8403 44431          fold           0              0              0              
    8407 44446          misleading     0              0              0              
    8412 44467          cases          0              0              0              
    8415 44478          fold           0              0              0              
    8416 44483          level          0              0              0              
    8418 44493          drop           0              0              0              
    8423 44515          data           0              0              0              
    8428 44534          shallowest     0              0              0              
    8429 44545          parts          0              0              0              
    8432 44556          section        0              0              0              
    8435 44571          equivalent     0              0              0              
    8442 44603          common         0              0              0              
    8444 44610          offset         0              0              0              
    8445 44617          section        0              0              0              
    8449 44635          S              0              0              0  
 
Removed words that contain Nouns, Verb, Adj, Adverbs, or Proper Names:
 ```python
# Remove all the words that are  not nouns, verbs, adj, adverbs, or proper names
        excluded_tags = {"NOUN", "VERB", "ADJ", "ADV", "ADP", "PROPN"}
        TextCleaned1 = [token for token in textAnalysis if excluded_tags]
        print(len(TextCleaned1))
        print(TextCleaned1)
```
Removed Stopwords and punctuation from the text:
 ```python
TextCleaned = [token for token in textAnalysis if not token.is_stop and not token.is_punct
                       and not token.is_space and not token.is_digit
                       and not token.like_num and not token.like_url and not token.like_email and token.is_alpha]
        DetectTitle = [token for token in textAnalysis if not token.text.istitle()]
        print(len(DetectTitle))
        print(DetectTitle)
```
