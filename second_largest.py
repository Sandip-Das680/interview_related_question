'''
Q6. Find second largest element
Input: [10, 5, 20, 8]
Output: 10

'''

def Second_max(lst):

    lst=sorted(lst)
    print(lst[-2])

def Second_max_opyimal(lst):
    if len(lst)<2:
        raise ValueError("lenght should be more than 2")
        return
    first =second =float('-inf')

    for val in lst:

        if val > first:
            second=first
            first=val
        elif val!=first and val> second:
            second=val
    return second

    

Input= [10, 5, 20, 8]
Second_max(Input)

print(Second_max_opyimal(Input))

