'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false'''

def Find_subsequence(s: str, t: str) -> bool:
    s_pointer=0
    flag = True

    for ch in t:
        if s_pointer> len(s)-1:
            break
        if s[s_pointer]==ch and s_pointer<len(s):
            s_pointer +=1
            flag=True
        else:
            flag = False

    return flag

def is_subsequence(s,t):
    s_pointer= 0

    for ch in t:

        if s_pointer ==len(s):
            break
        if s[s_pointer]==ch:
            s_pointer+=1

    return s_pointer==len(s)

s = "axc"
t = "ahbgdc" 

print(Find_subsequence(s,t))

