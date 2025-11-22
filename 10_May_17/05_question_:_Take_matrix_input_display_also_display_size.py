'''
Q. Write a Python program that:
Takes the number of rows and columns as input,
Accepts matrix elements from the user,
Prints the matrix in a clean format, and
Displays the total number of elements in the matrix,
Using a modular approach (i.e., a separate function to compute matrix size).
'''


# Function to calculate total number of elements in a matrix
def matrix_size(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    return rows * cols


def main():
    # Step 1: Input dimensions
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    # Step 2: Input matrix elements
    print("\nEnter the matrix elements:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Element at ({i},{j}): "))
            row.append(value)
        matrix.append(row)

    # Step 3: Display the matrix
    print("\nMatrix:")
    for row in matrix:
        print(row)

    # Step 4: Display matrix size
    print("\nTotal matrix size:", matrix_size(matrix))


# Run the program
main()
