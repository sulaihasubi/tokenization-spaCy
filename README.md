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


