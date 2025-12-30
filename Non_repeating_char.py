'''
imput = progamming"
Output ='p'

'''
from collections import Counter

def Non_repeating_char(word):

    freq={}

    for ch in word:
        freq[ch]= freq.get(ch,0)+1
    print(freq)
    for ch in freq:
        if freq[ch]==1:
            print(ch)
            break


imput="programming"

freq_ch= Counter(imput)

for ch in freq_ch:
    if freq_ch[ch]==1:
        print(ch)
        break
Non_repeating_char(imput)

