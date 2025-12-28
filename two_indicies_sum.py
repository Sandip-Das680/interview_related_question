'''
two sum problem

nums = [2, 7, 11, 15]
target = 9
output=[0,1]
'''
def two_sum(lst, target):
    seen={}

    for i , num in enumerate(lst):
        diff = target - num
        if diff in seen:
            return[seen[diff],i]
        seen[num]=i
    return []
nums = [2, 7, 11, 15]
target = 11

print(two_sum(nums,target))
