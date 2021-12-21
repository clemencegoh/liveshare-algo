## Workspace for sessions and algo solving drafts

### Session 4 warm-up - is pallindrome

"""
Given a string - return true if is pallindrome.
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise

Examples:

---

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

---

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""
def isPallindrome(s: str):
  pass

assert isPallindrome("A man, a plan, a canal: Panama") == True
assert isPallindrome("race a car") == False
assert isPallindrome(" ") == True



## Session 4 concept - Stacks 
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Examples:

---
Input: s = "()"
Output: true

---
Input: s = "()[]{}"
Output: true

---
Input: s = "(]"
Output: false

"""

def isValid(s: str):
  pass

assert isValid('()') == True
assert isValid('(]') == False
assert isValid('(())[]{}') == True
assert isValid('([]{)}') == False
assert isValid('(([[{{}}]]))[]') == True