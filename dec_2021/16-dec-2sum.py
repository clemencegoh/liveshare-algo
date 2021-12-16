# Q: 2Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

## arr[i] + arr[j] == target

# O(1)
# log(n)
# n
# n^2 ... n^const
# n^n
# 2^n
# n!

##  Q: 3Sum ?  Deferred
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


# Space: O(1)  ==> O(n)
# Time: O(n**2)  ==> O(n)
def twoSum(arr, target):
    ans = []
    ref = dict()  # { 7: 0, 2: 1, -2: 2, -6: 3 }  len(key) == n, len(value) == n   Space: O(n)
    for i, item in enumerate(arr):  # O(n)
        if item in ref:  # O(1)
            ans.append([ref[item], i])
        ref[target - item] = i
            
    return ans


# person = { 'name': '', 'age': '26' }  ==> person['name'] O(1) 

example = [2,7,11,15]
example2 = [1,2,3,4,5]
target = 9
target2 = 3

examples = [example, example2]
targets = [target, target2]
answers = [ [[0,1]], [[0, 1]] ]

def driver():
    for i in range(len(examples)):
        print(twoSum(examples[i], targets[i]))
        print(f'====> Actual: {answers[i]}')

driver()
