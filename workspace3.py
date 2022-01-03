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


from misc.singlyLinkedListNode import SingleListNode, generate_from_array


# def maxProfit(arr):
#     pass


# assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
# assert maxProfit([7, 6, 4, 3, 1]) == 0
# assert maxProfit([1, 2, 3, 4, 5, 6]) == 5
# print("complete")


# Main question of the day - Maximum subarray
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

(moving array)

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
---

Example 2:

Input: nums = [1]
Output: 1
---

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""


# def maxArray(arr):
#     pass


# assert maxArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
# assert maxArray([1]) == 1
# assert maxArray([5, 4, -1, 7, 8]) == 23
# print("complete")
