#Insertion Sort 
def main():
    arr = []
    n = int(input())
    while len(arr) != n:
        item = list(map(int, input().split()))
        arr.extend(item)
        print('unsorted array is: ',arr)
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        while arr[j] > current and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

    print('sorted array is: ',arr)


main()
