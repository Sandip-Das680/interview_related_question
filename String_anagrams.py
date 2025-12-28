'''
Check if two strings are anagrams
Input: "listen", "silent"
Output: True

'''

def check_anagrams(word1: str, word2:str):

    word1=sorted(word1)
    word2=sorted(word2)

    if word1 == word2:
        print("both words are anagrams")
    else:
        print("both words are not anagrams")

def check_anagrams_optimal(word1: str, word2: str):

    if len(word1)!=len(word2):
        print("both words are not anagrams")
        return
    freq={}

    for ch in word1:
        freq[ch]= freq.get(ch, 0)+1

    print(freq)

    for ch in word2:
        if ch not in freq or freq[ch]==0:
            print("both words are not anagrams")
            return
        freq[ch]-=1
    print("both words are anagrams")
    

        

word1="listen"
word2="silent"

check_anagrams(word1,word2)
check_anagrams_optimal(word1,word2)


