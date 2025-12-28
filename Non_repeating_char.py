'''
imput = progamming"
Output ='p'

'''
from collections import Counter

imput="programming"

freq_ch= Counter(imput)

for ch in freq_ch:
    if freq_ch[ch]==1:
        print(ch)
        break