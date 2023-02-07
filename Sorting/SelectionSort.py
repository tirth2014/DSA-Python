#selection sort
import sys

def selSort(arr,n):
    for i in range(n):
        currMin = sys.maxsize
        for j in range(i,n):
            if arr[j] < currMin:
                currMin=arr[j]
                ind=j
        arr[i],arr[ind] = arr[ind],arr[i]
    return arr
def main():
    lst=[]
    n=int(input())
    for i in range(n):
        lst.append(int(input()))
    print('original list: ', lst)
    print('sorted list: ',selSort(lst,n))

main()
