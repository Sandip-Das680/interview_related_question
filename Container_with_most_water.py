'''

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

'''

def Max_water(lst):
    left=0
    right = len(lst)-1
    max_area = 0

    while left < right :
        width = right-left
        length= min(lst[left],lst[right])
        area = width * length

        max_area= max(max_area,area)

        if lst[left]< lst[right]:
            left+=1
        else:
            right-=1

    return max_area

height = [1,8,6,2,5,4,8,3,7]

print(Max_water(height))
