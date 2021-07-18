### Python Developer: Sulaiha Subi ###
### NLP Version 1.5: 5th July 2021###
### Python Version: 3.9 ###

# Making Connection Mongodb
import namelist as namelist
import requests
from numpy import info
from pip._internal.utils import logging
from pymongo import MongoClient
import re
from io import BytesIO

myclient = MongoClient("mongodb://localhost:27017/")
# Database
db = myclient["RiseHill"]
# Created or Switched to collection
Collection = db["FilesCollection"]


#### Import Library Here: ####
# Reading the contents of the folder. Read the txt file(unclean text). Uncomment below.
# with open('/Users/risehill/Documents/09-NLPProcessing/TextExtracted/ExtractedText.txt') as f:
#     textfile = f.read()
    # print(textfile)

# spaCy Code Initialization:
import glob
import spacy

nlp = spacy.load(name='en_core_web_sm')

# To customize tokenization by updating the tokenizer property on the nlp object
import re
custom_nlp = spacy.load(name='en_core_web_sm')
prefix_re = spacy.util.compile_prefix_regex(custom_nlp.Defaults.prefixes)
suffix_re = spacy.util.compile_suffix_regex(custom_nlp.Defaults.suffixes)
infix_re = re.compile(r'''[-~]''')

path = '/Users/risehill/Documents/09-NLPProcessing/TextExtracted/Zul.txt'
# Note that this is just a generator (doc.sents). Read the file path, uncomment below.
# for sent in doc.sents:
#     print(sent.text)

# Process 1: spaCy Process (Tokenization → Lemmatization → Remove stopwords → Remove punctuation)
# Sub-Process 1.1: Tokenization and Lemmatization → Remove Stopwords
# text_with_ws prints token text with trailing space (if present)
# is_alpha detects if the token consists of alphabetic characters or not.
# is_punct detects if the token is a punctuation symbol or not.
# is_space detects if the token is a space or not.
# shape_ prints out the shape of the word.
# is_stop detects if the token is a stop word or not.
# pos detects their Parts-of-speech tags.
# lemma_ detects Lemmatization. Lemmatization is the process of retrieving the root word of the current word.
# tag_ lists the fine-grained part of speech.

# Get the content from Text Files
file_lines = []
no_texts = []
text_cleans = []

# Process 1: Text Preprocessing

for file in glob.glob(path):
    with open(file, encoding='utf-8', errors='ignore') as file_in:
        text = file_in.read()
        lines = text.split('\n')
        # Process the line in some way
        file_lines.append(lines[0])
        # Read the file line by line (Get the title of the report)
        # print(lines[0])

        # Replace the newline as one string
        Newtext = text.replace('\n', ' ')
        # Check number of text contents in original Text files
        # print(len(Newtext))
        # print(Newtext)
        # print(len(text))

        # Removing stopwords and punctuation from the text
        textAna = Newtext
        textAnalysis = nlp(textAna)
        textAnalysis2 = nlp(text)

        # Checking the document level
        ents = [(e.text, e.kb_id_) for e in textAnalysis.ents]
        # print(ents)

        # Removed the entity PERSON in the text : 853
        ents2 =[ee for ee in textAnalysis.ents if ee.label_ != 'PERSON']
        # print(len(ents2))
        # print(ents2)
        # to display the visualisation of not contain NER Person
        # displacy.serve(ents2, style="ent")

        # Remove all the words that are  not nouns, verbs, adj, adverbs, or proper names
        excluded_tags = {"NOUN", "VERB", "ADJ", "ADV", "ADP", "PROPN"}
        TextCleaned1 = [token for token in textAnalysis if excluded_tags]
        # print(len(TextCleaned1))
        # print(TextCleaned1)


        # Removed Stopwords and punctuation from the text : 5247
        TextCleaned = [token for token in textAnalysis if not token.is_stop and not token.is_punct
                       and not token.is_space and not token.is_digit
                       and not token.like_num and not token.like_url and not token.like_email and token.is_alpha]
        DetectTitle = [token for token in textAnalysis if not token.text.istitle()]
        # print(len(DetectTitle))
        # print(DetectTitle)

        # To check the number of text after removing the stopwords and punctuation
        print(len(TextCleaned))
        no_texts.append(len(TextCleaned))
        # print(TextCleaned)


        # Convert Clean Tokens into string
        # for i in TextCleaned:
        #     print(i, end=' ')
            # print(' '.join(map(str, TextCleaned)))
        CleanTextLowerCase = (' '.join(map(str, TextCleaned)))
        # change the string to lower case
        CleanText = CleanTextLowerCase.lower()
        print(CleanText)


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
                # print(analyzeToken5)

# for i in range(len(no_texts)):
#     print(no_texts[i])

# Process 2: Getting the metadata and send to MongoDb
data = []
mainData = {} #creating the dictionary to send inside the mongodb
for i in range(len(file_lines)):
        file_line = file_lines[i]
        no_text = no_texts[i]
        text_clean = text_cleans[i]
        file = {"Report Title": file_line,
        "No Cleaned Text" : no_text,
         "Cleaned Text" : text_clean
        }
        data.append(file)

# Import into the mongodb
# for i in range(len(data)):
#     mainData['Text File' + str(i+1)] = data[i]
# Collection.insert_one(mainData)
