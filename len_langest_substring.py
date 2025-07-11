'''Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''
def lenOfLongest_subString(str):
    max_len=0
    start=0
    char_set=set()
    for char in range(len(str)):
        while str[char] in char_set:
            char_set.remove(str[start])
            start+=1
        char_set.add(str[char])   
        max_len=max(max_len,char-start+1) 
    return max_len    

    
str=input("Enter the string")
print(lenOfLongest_subString(str))


