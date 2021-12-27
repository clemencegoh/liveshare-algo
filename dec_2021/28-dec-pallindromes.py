### Session 4 warm-up - is pallindrome

"""
Given a string - return true if is pallindrome.
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise

(python string prototype contains .isalnum() to determine if it is alphanumeric)

.isupper()
.islower()

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

# Time: O(n)
def isPallindrome(s: str):
    lower_s = s.lower()

    ptr = 0
    while ptr < len(lower_s):
        if not lower_s[ptr].isalnum():
            lower_s = lower_s[:ptr] + lower_s[ptr + 1 :]
        else:
            ptr += 1

    if len(lower_s) % 2:  # is odd
        middle = int(len(lower_s))
        left = lower_s[:middle]
        right = lower_s[middle + 2 :: -1]

    else:  # is even
        middle = int(len(lower_s))
        left = lower_s[:middle]
        right = lower_s[middle + 1 :: -1]

    if left == right:
        return True
    else:
        return False


def isPallindromeV2(s: str):
    ptr_front = 0
    ptr_back = len(s) - 1
    while ptr_front < ptr_back:
        while not s[ptr_front].isalnum():
            ptr_front += 1
        while not s[ptr_back].isalnum():
            ptr_back -= 1

        if s[ptr_front].lower() != s[ptr_back].lower():
            return False
        ptr_front += 1
        ptr_back -= 1
    return True


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

    dict1 = {}

    for i in s:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1

    num_odds = 0
    for keys, value in dict1.items():
        if value % 2:  # if odd
            num_odds += 1
        if num_odds > 1:
            return False

    return True


print(pallindromePerm("code"))
assert pallindromePerm("code") == False
assert pallindromePerm("aab") == True
assert pallindromePerm("carerac") == True
print("iz correct")


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

    dict1 = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    mainarr = []

    for i in s:
        if i == "(" or i == "{" or i == "[":
            mainarr.append(i)

        elif i in dict1:
            if mainarr[-1] == dict1[i]:
                mainarr.pop()
            else:
                return False

    return True


assert isValid("()") == True
assert isValid("(]") == False
assert isValid("(())[]{}") == True
assert isValid("([]{)}") == False
assert isValid("(([[{{}}]]))[]") == True
print("complete")
