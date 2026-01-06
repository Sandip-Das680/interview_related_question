'''

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 
 '''
def move_zeros(nums):

    if len(nums) <= 1:
        return nums
    
    for i in range(0, len(nums)):

        for j in range(i, len(nums)-1):

            if nums[j]==0:
                nums[j],nums[j+1]=nums[j+1], nums[j]
    return nums

def Move_zero_optimal(nums):

    pos=0

    for i in range(0,len(nums)):
        if nums[i]!=0:
            nums[pos]=nums[i]
            pos+=1

    for i in range(pos,len(nums)):
        nums[i]=0

    return nums

nums = [0,1,0,3,12]

print(Move_zero_optimal(nums))
