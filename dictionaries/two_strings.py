'''
Given two strings, determine if they share a common substring. 
A substring may be as small as one character.
For example, the words "a", "and", "art" share the common substring a. 
The words "be" and "cat" do not share a substring.

Function Description
Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on whether the strings share a common substring.
twoStrings has the following parameter(s):
s1, s2: two strings to analyze .
'''

def twoStrings(s1, s2):
    #example of set intersections
    return 'YES' if set(list(s1)) & set(list(s2)) != set() else 'NO'