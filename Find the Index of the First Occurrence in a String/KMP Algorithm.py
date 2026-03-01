'''
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.

Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.
'''
#KMP Algorithm
def strStr(haystack, needle):
    if not needle:
        return 0

    # Build LPS array
    lps = [0] * len(needle)
    length = 0
    i = 1
    
    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # Pattern matching
    i = j = 0  # i for haystack, j for needle
    
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        
        if j == len(needle):
            return i - j
        
        elif i < len(haystack) and haystack[i] != needle[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1
# Example usage
print(strStr("sadbutsad", "sad"))  # Output: 0
print(strStr("leetcode", "leeto"))  # Output: -1