'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
'''

def max_sum(nums, k):

    win_size=k
    i=0
    max_avg=float('-inf')
    

    while win_size <len(nums):
        sum=0.0
        j=i

        while j < win_size:
            sum+=nums[j]
            j+=1
        avg=float(sum/k)
        max_avg=max(avg,max_avg)
        i+=1
        win_size+=1
    return max_avg


def max_sum_Optimal(nums, k):
    win_sum = sum(nums[:k])

    max_sum=win_sum

    for i in range(k, len(nums)):
        win_sum+=nums[i]
        win_sum-=nums[i-k]

        max_sum = max(win_sum,max_sum)

    return max_sum/k






nums = [1,12,-5,-6,50,3]
k = 4

print(max_sum(nums,k))
print(max_sum_Optimal(nums,k))
