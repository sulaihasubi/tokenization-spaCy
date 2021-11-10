Tokenization using spaCy
========================

Introduction
------------
Tokenizer is a tool that splits a given text into tokens using regular expressions. The process of tokenizing a text into segments of words and punctuation in Spacy is done in several processes. It reads text from left to right. To begin, the tokenizer separated the text on whitespace in the same way that the split() method does. The tokenizer then checks to see whether the substring fits the tokenizer exception rules.

Installation for macOS:

```
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
```
Installation for other operating system, can be refer [here](https://spacy.io/usage)
