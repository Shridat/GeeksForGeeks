class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        min_idx = 0
        max_idx = n-1
        max_ele = arr[max_idx]+1
        
        for i in range(n):
            if i%2==0:
                arr[i] += (arr[max_idx]%max_ele)*max_ele
                max_idx-=1
            else:
                arr[i]+=(arr[min_idx]%max_ele)*max_ele
                min_idx+=1
        for i in range(n):
            arr[i]//=max_ele
