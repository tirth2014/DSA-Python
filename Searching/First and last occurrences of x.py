"""
Approach: Two pointer
Time Complexity: O(n)
Space Complexity: O(1)
"""

def find(arr,n,x):
    first = last = -1
    left, right = 0, n - 1

    while left <= right:
        if arr[left] == x and arr[right] == x:
            first = left
            last = right
            break
        if arr[left] != x:
            left += 1
        if arr[right] != x:
            right -= 1
    return first, last



'''
Approach: Binary Search
Time Complexity: O(logn)
Space Complexity: O(1)
'''
def firstOccurence(arr,n,x):
    l,r = 0,n-1
    first = -1
    while l <= r:
        m = l + (r-l)//2
        if arr[m] == x:
            first = m
            r = m-1
        elif x < arr[m]:
            r = m-1
        else:
            l = m+1
    return first
        
def lastOccurence(arr,n,x):
    l,r = 0,n-1
    last = -1
    while l <= r:
        m = l + (r-l)//2
        if arr[m] == x:
            last = m
            l = m+1
        elif x < arr[m]:
            r = m-1
        else:
            l = m+1
            
    return last

def find(arr,n,x):
    first = firstOccurence(arr,n,x)
    last =  lastOccurence(arr,n,x)
    return first,last
        

#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends
