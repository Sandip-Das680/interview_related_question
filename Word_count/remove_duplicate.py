'''
Q5. Remove duplicates while preserving order
Input: [1, 2, 2, 3, 1]
Output: [1, 2, 3]

'''

def remove_duplicate(lst):
    res=[]
    res.append(lst[0])

    for ch in lst:
        if ch in res:
            continue
        else:
            res.append(ch)
    print(res)

def remove_duplicate_optimal(lst):

    seen=set()
    res=[]

    for ch in lst:
        if ch not in seen:
            seen.add(ch)
            res.append(ch)
    print(res)

input_list=[1, 2, 2, 3, 1]

remove_duplicate(input_list)

remove_duplicate_optimal(input_list)