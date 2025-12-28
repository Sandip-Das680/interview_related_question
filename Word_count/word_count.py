'''
Count frequency of characters (without Counter)

'''

import string

def word_count(word: str):
    words=word.split()

    freq={}

    for ch in words:
        freq[ch]= freq.get(ch, 0)+1
    
    for ch, count in freq.items():
        print(f"{ch}={count}")

def word_count_Optimal(sentence:str):

    freq= {}
    for ch in sentence.lower().split():
        ch=ch.strip(string.punctuation)
        freq[ch]= freq.get(ch, 0)+1

    for ch, count in freq.items():
        print(f"{ch}={count}")



text = " krishanu#$@ techno work i in techno krishanu"
res=text.split(',')
new_res=" ".join(res)
word_count(new_res)
print(new_res)

word_count_Optimal(text)
