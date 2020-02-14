print("############## NEW DATA ##############")
print("##################################")
print()
raw_data = open("SMSSpamCollection").read()
print(raw_data[0:500])

print("############## NEW DATA ##############")
print("##################################")
print()

parse_data = raw_data.replace("\t" , "\n").split("\n")
print(parse_data[0:10])



print("############## NEW DATA ##############")
print("##################################")
print()
label_list = parse_data[0::2]
msg_list = parse_data[1::2]
print(label_list[0:5])
print(msg_list[0:5])

print("############## NEW DATA ##############")
print("##################################")
print() 

import pandas as pd


table_frame = pd.DataFrame({

    "label" : label_list[:-1] ,
    "SMS" : msg_list

    })

print(table_frame.head())

print()
print("############## NEW DATA ##############")
print("##################################")
print()


# METHOD TWO OF IMPORTING DATA

pd.set_option("display.max_colwidth" , 50)
dataset  = pd.read_csv("SMSSpamCollection" , sep="\t" , header=None)
print(dataset.head())



print()
print("############## NEW DATA ##############")
print("##################################")
print()

##  EXPLORING THE DATASET......

dataset.columns = ["Label" , "SMS"]
print(dataset.head())

print(f"data set contain {len(dataset)} row ... {len(dataset.columns)} colums")



print()
print("############## NEW DATA ##############")
print("##################################")
print() 

##  REMOVING PUNCTUATION......

import string

def remove_punctuation(text):
    punct = "".join([c for c in text if c not in string.punctuation]) 
    return punct


dataset["c_sms"] = dataset["SMS"].apply(lambda x: remove_punctuation(x))
print(dataset.head())



print()
print("############## NEW DATA ##############")
print("##################################")
print() 

from nltk.tokenize import word_tokenize

##  tokenize data ......

def tokenize_word(text):
    return word_tokenize(text)

dataset["c_sms_token"] = dataset["c_sms"].apply(lambda x: tokenize_word(x.lower()))
print(dataset.head())




print()
print("############## NEW DATA ##############")
print("##################################")
print() 

from nltk.corpus import stopwords

st = stopwords.words("english")
print(st[0:10])
##  tokenize data ......

def remove_stopword(text):
    word = [wd for wd in text if wd not in st]
    return word

dataset["c_sms_clean_stop"] = dataset["c_sms_token"].apply(lambda x: remove_stopword(x))
print(dataset.head())




print()
print("############## NEW DATA ##############")
print("##################################")
print() 

##  lemmertizing word for preprocessing

from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()

print(dir(lemma))

def lemmatization(text):
    lem_word = [lemma.lemmatize(word) for word in text if text]
    return lem_word


dataset["lemma_ sms"] = dataset["c_sms_clean_stop"].apply(lambda x: lemmatization(x))

print(dataset.head())



print()
print("############## NEW DATA ##############")
print("##################################")
print() 

##  Vectorization 

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()

corpus = ["this is a sentence is" ,
          "this is another sentence" ,
          "third document is here"]


X = cv.fit(corpus)
print(cv.get_feature_names())
print(X.vocabulary_)


X = cv.transform(corpus)
print(X.shape)
print(X.toarray())

dat = pd.DataFrame(X.toarray() , columns=cv.get_feature_names())
print(dat.head())






print()
print("############## NEW DATA ##############")
print("##################################")
print() 

##  Vectorization 

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()

corpus = ["this is a sentence is" ,
          "this is another sentence" ,
          "third document is here"]


X = cv.fit(corpus)
print(cv.get_feature_names())
print(X.vocabulary_)


X = cv.transform(corpus)
print(X.shape)
print(X.toarray())

dat = pd.DataFrame(X.toarray() , columns=cv.get_feature_names())
print(dat.head())

















 
