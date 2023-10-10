# 2.create of pyramid of numbers from 1 to 20 using python
def pyramid(no_row): # Define the maximum number in the pyramid
    # Loop through rows
    for outer_row in range(1, no_row + 1):
        # Print spaces before the numbers
        for column in range(no_row, outer_row, -1):
            print(" ", end=" ")
        # Print numbers in ascending order
        for num_asc in range(1, outer_row + 1):
            print(num_asc, end=" ")
        # Print numbers in descending order
        for num_desc in range(outer_row - 1, 0, -1):
            print(num_desc, end=" ")

        # Move to the next line
        print()
pyramid(20)