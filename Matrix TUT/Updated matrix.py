def read_matrix_dimension():
    """Reads matrix dimension values from user"""
    while True:
        dimension_str = input("Enter matrix dimensions (e.g. 2x3 or 4x5): ")
        try:
            rows, cols = map(int, dimension_str.split("x"))
            return rows, cols
        except ValueError:
            print("Invalid input, please try again")

def read_matrix_values(rows, cols):
    """Reads matrix values from user"""
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                value_str = input(f"Enter value for row {i+1}, column {j+1}: ")
                try:
                    value = float(value_str)
                    row.append(value)
                    break
                except ValueError:
                    print("Invalid input, please try again")
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    """Displays matrix values"""
    print("Matrix:")
    for row in matrix:
        print(" ".join(str(value) for value in row))

def multiply_matrix(matrix, multiplier):
    """Multiplies matrix values based on user input and displays the new matrix"""
    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value * multiplier)
        new_matrix.append(new_row)
    print(f"Matrix multiplied by {multiplier}:")
    display_matrix(new_matrix)

# Main program
rows, cols = read_matrix_dimension()
matrix = read_matrix_values(rows, cols)
display_matrix(matrix)
multiplier_str = input("Enter a value to multiply the matrix: ")
try:
    multiplier = float(multiplier_str)
    multiply_matrix(matrix, multiplier)
except ValueError:
    print("Invalid input, matrix not multiplied")
