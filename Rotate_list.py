'''
Q7. Rotate list by k steps
Input: [1,2,3,4,5], k=2
Output: [4,5,1,2,3,6]
'''

def rotate_list(lst, n):
    res=[]

    n = n % len(lst)

    for i in range(len(lst)-n, len(lst)):
        res.append(lst[i])
    for i in range(0,len(lst)-n):
        res.append(lst[i])

    print(res)

Input=[1,2,3,4,5]
k=13
rotate_list(Input,k)

        
    
