if __name__ == "__main__":
  
    def print_matrix(matrix):
        for row in matrix:
            print(' '.join(map(str, row)))

    # Taking input from the user
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    mat = []
    for i in range(rows):
        row = list(map(int, input(f"Enter space-separated values for row {i + 1}: ").split()))
        mat.append(row)

    print("Input Matrix:")
    print_matrix(mat)
