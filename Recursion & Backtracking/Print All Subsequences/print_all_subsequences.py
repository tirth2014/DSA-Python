# Ref: https://www.youtube.com/watch?v=AxNNVECce8c&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=6 [Striver - L6. Recursion on Subsequences | Printing Subsequences]

# Print all non-contagious subsequences using recursion.
def get_subsequences(i,ds,arr,n):
    # BASE CASE
    # If index is equal to input array length print the data structure containing subsequence
    if i == n:
        print(ds,end="  ")
        return

    # Case-1: Take/Pick the particular index into the subsequence
    ds.append(arr[i])
    get_subsequences(i+1,ds,arr,n)
    ds.remove(arr[i])

    # Case-2: Not Take/Not Pick the particular index into the subsequence
    get_subsequences(i+1,ds,arr,n)


if __name__ == '__main__':
    a = [3,1,2]
    ds = []
    get_subsequences(0,ds,a,len(a))
    
# OUTPUT: [3, 1, 2]  [3, 1]  [3, 2]  [3]  [1, 2]  [1]  [2]  [] 


# TIME COMPLEXITY
# Exponential - O(2^n) as at each index 2 recursive calls are made: one with current index picked and another without picked.

# SPACE COMPLEXITY
# O(n) which is depth of the recursion tree
