'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
'''

from collections import defaultdict

def find_pair(nums, target):

    freq= defaultdict(int)
    print(freq)
    count=0

    for val in nums:
        diff = target-val
        print(freq[diff])

        if freq[diff] > 0:
            count += 1
            freq[diff] -= 1
        else:
            freq[val] += 1

    return count
    

def maxOpertion_using_pointer(nums,k):

    left, right =0, len(nums)-1
    count =0
    nums.sort()

    while left <right:
        current_sum= nums[left]+nums[right]

        if current_sum == k:
            count+=1
            left+=1
            right-=1
        elif current_sum < k:
            left+=1
        else:
            right-=1
    return count

nums=[4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2

print(maxOpertion_using_pointer(nums,k))

print("*******")

print(find_pair(nums,k))



