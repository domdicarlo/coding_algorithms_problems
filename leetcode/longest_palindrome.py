from math import floor

"""

Longest Palindromic Substring - Leetcode Question #5

Question URL: https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Solution:

I went ahead and pursued a solution where we look at each "center" of a palindrome. 
A palindrome can be centered either on a letter, or in between letters. 
In both cases, the goal is to check letters on the left and right two by two,
and check if they are equal as we build a palindrome. If they are,
we keep going and track how big the palindrome is. If they aren't, we stop and
record the longest palindrome.

This only takes N^2 time and constant aux space (where N is the length of the string).
It takes N^2 time since for each center, we need to do a max of 
N/2 letter comparisons, which take O(1) time.

We have (2N - 1) centers: N letters and N-1 spaces in between letters.

"""

def longestPalindrome( s: str) -> str:
    # for empty case:
    if s == "":
        return ""
    
    longest_streak = 1
    # longest palindrome is at least one letter long
    longest_palindrome = s[0]

    # find all palindromes with a center on a letter
    for i in range(0, len(s)):
        streak = 1
        for j in range(0, min(i, len(s) - (i + 1))):
            if s[i - j - 1] == s[i + j + 1]:
                streak += 2
            else:
                break
        if streak > longest_streak:
            longest_streak = streak
            start_of_word = i - floor((longest_streak - 1) / 2)
            longest_palindrome = s[start_of_word:start_of_word + longest_streak]

    # find all palindromes with a center in between letters
    for i in range(0, len(s) - 1):
        streak = 0
        for j in range(1, min(i + 2, len(s) - i)):
            if s[i - j + 1] == s[i + j]:
                streak += 2
            else:
                break
        if streak > longest_streak:
            longest_streak = streak
            start_of_word = (i + 1) - floor(longest_streak / 2)
            longest_palindrome = s[start_of_word:start_of_word + longest_streak]

    return longest_palindrome


