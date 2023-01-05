import spacy
nlp = spacy.load('en_core_web_md')
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

tokens1 = nlp("king queen castle")
tokens2 = nlp("queen prince throne")

for token1 in tokens1:
    for token2 in tokens2:
        print(token1.text, token2.text, token1.similarity(token2))

'''It's interesting to note that the 
similarity scores between the words 
"cat" and "monkey", and "apple" and "banana" 
are relatively high, despite not being
 closely related semantically. 
'''
