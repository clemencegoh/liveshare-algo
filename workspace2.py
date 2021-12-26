## Secondary workspace


### Session 4 warm-up - is pallindrome

"""
Given a string - return true if is pallindrome.
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise

(python string prototype contains .isalnum() to determine if it is alphanumeric)

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
from typing import List


def isPallindrome(s: str):
    pass


assert isPallindrome("A man, a plan, a canal: Panama") == True
assert isPallindrome("race a car") == False
assert isPallindrome(" ") == True


## Session 4 warm-up - pallindrome permutation
"""
Given a string s, return true if a permutation of the string could form a palindrome.

Examples:

---
Input: s = "code"
Output: false

---
Input: s = "aab"
Output: true

---
Input: s = "carerac"
Output: true

"""


def pallindromePerm(s: str):
    pass


assert pallindromePerm("code") == False
assert pallindromePerm("aab") == True
assert pallindromePerm("carerac") == True


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


assert isValid("()") == True
assert isValid("(]") == False
assert isValid("(())[]{}") == True
assert isValid("([]{)}") == False
assert isValid("(([[{{}}]]))[]") == True


## Concept - Array lookback
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Examples:

---
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

---
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""


def maxProfit(arr: List[int]):
    pass


assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert maxProfit([7, 6, 4, 3, 1]) == 0
assert maxProfit([1, 2, 3, 4, 5, 6]) == 5
