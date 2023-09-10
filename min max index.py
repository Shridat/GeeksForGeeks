import math

def find(arr,n,x):
    # code here
    if x not in arr:
        return -1,-1
    min_idx = math.inf
    max_idx = -math.inf
    for i in range(len(arr)):
        if arr[i]==x:
            min_idx = min(min_idx,i)
            max_idx = max(max_idx,i)
    return min_idx,max_idx
'''
nput:
n=9, x=5
arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
Output:  
2 5
Explanation: 
First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5. 
'''
