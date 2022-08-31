class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (self.n + 1)

    def update(self, i, x):
        while i <= self.n:
            self.bit[i] += x  # (i&-i,i) gives the first rightmost SET bit of the number in binary
            i += i & -i

    def sum(self, i):
        ans = 0
        while i > 0:
            ans += self.bit[i]
            i -= i & -i
        return ans


if __name__ == "__main__":
    arr = list(map(int, input("enter array elements with comma in between: ").strip().split(',')))
    tree = BIT(len(arr))
    print("Input List with Index: ", {i : arr[i] for i in range(len(arr))})
    for i in range(1, len(arr) + 1):
        tree.update(i, arr[i - 1])
    print('The BIT is: ', {i: tree.bit[i] for i in range(len(tree.bit))})
    # The ith bit stores the sum from j+1 to i where j = i-(i&-i)
    i = int(input("Enter the index: "))
    res = tree.sum(i)
    print("The sum of elements till {0} is {1}".format(i, res))
    i = int(input("Enter the index to Update the value at: "))
    x = int(input("enter the value to be added at index {0}: ".format(i)))
    tree.update(i, x)
    print('The updated BIT is: ', {i: tree.bit[i] for i in range(len(tree.bit))})
    i = int(input("Enter the index till which you want sum: "))
    res = tree.sum(i)
    print("The sum of elements till {0} after updation is: {1}".format(i, res))
