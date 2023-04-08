arr = [5, 3, 7, 9, 1, 2, 4]


def reverse_arr(arr, i, n):
    if i >= n // 2: return arr
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return reverse_arr(arr, i + 1, n)


res = reverse_arr(arr, 0, len(arr))
print(res)
