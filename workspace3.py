## Secondary workspace


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


# def maxProfit(arr: List[int]):
#     pass


# assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
# assert maxProfit([7, 6, 4, 3, 1]) == 0
# assert maxProfit([1, 2, 3, 4, 5, 6]) == 5


def isValid(s: str):
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    store = []
    for bracketType in s:
        if bracketType in brackets:
            store.append(bracketType)
        else:
            if brackets[store[-1]] != bracketType:
                return False
            store.pop()
    return len(store) == 0


assert isValid("()") == True
assert isValid("(]") == False
assert isValid("(())[]{}") == True
assert isValid("([]{)}") == False
assert isValid("(([[{{}}]]))[]") == True
print("complete")
