'''
Q2. Reverse words in a sentence
Input: "IBM is a great company"
Output: "company great a is IBM"

'''

def reverse_word(word):

    words=word.split()
    
    new_word=words[::-1]
    
    return " ".join(new_word)

Input= "IBM is a great company"

print(reverse_word(Input))