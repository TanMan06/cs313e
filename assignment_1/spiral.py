"""
File:spiral.py
Description:
Student Name: Tanner Jackson
Student EID: twj393
Partner Name: Shanmukha Pinapati
Partner UT EID : ssp3428
Course Name : CS 313E
Unique Number : 50183
Date Created : 8/28/24
Date Last Modified: 8/28/24
Input: S1 and S2 are two Strings of DNA
Output: Return the longest subtring of DNA between each pair of strands

 Input: n is an odd integer between 1 and 100
 Output: returns a 2-D list representing a spiral
         if n is even add one to n

def create_spiral(n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")

 Input: spiral is a 2-D list and n is an integer
 Output: returns an integer that is the sum of the
         numbers adjacent to n in the spiral
         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")
"""

def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral dimeter"""
    mat = [[0 for _ in range(dim)] for _ in range(dim)]
    x_pos = dim//2
    y_pos=dim//2
    cnt=1
    steps_to_move = 1
    for _ in range(dim):
        for _ in range (steps_to_move):
            mat[y_pos][x_pos] = cnt
            cnt+=1
            x_pos+=1
        for _ in range (steps_to_move):
            if not isvalid(y_pos,x_pos,mat):
                return mat
            mat[y_pos][x_pos] = cnt
            cnt+=1
            y_pos+=1
        steps_to_move+=1
        for _ in range (steps_to_move):
            mat[y_pos][x_pos] = cnt
            cnt+=1
            x_pos-=1
        for _ in range (steps_to_move):
            mat[y_pos][x_pos] = cnt
            cnt+=1
            y_pos-=1
        steps_to_move+=1
    return mat


def sum_sub_grid(grid, val):
    """
    Input: grid a 2-D list containing a spiral of numbers
           val is a number within the range of numbers in
           the grid
    Output:
    sum_sub_grid returns the sum of the numbers (including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """
    i = 0
    j = 0
     # Initializing x_pos1
    for _ in range(len(grid)):
        for _ in range (len(grid[i])):
            if val == grid[i][j]:
                x_pos = i
                y_pos = j
            j+=1
        i+=1
        j=0
    cnt = 0
    if isvalid(x_pos+1, y_pos, grid):
        cnt+=grid[x_pos+1][y_pos]
    if isvalid(x_pos+1, y_pos+1, grid):
        cnt+=grid[x_pos+1][y_pos+1]
    if isvalid(x_pos+1, y_pos-1, grid):
        cnt+=grid[x_pos+1][y_pos-1]
    if isvalid(x_pos, y_pos+1, grid):
        cnt+=grid[x_pos][y_pos+1]
    if isvalid(x_pos, y_pos-1, grid):
        cnt+=grid[x_pos][y_pos-1]
    if isvalid(x_pos-1, y_pos+1, grid):
        cnt+=grid[x_pos-1][y_pos+1]
    if isvalid(x_pos-1, y_pos, grid):
        cnt+=grid[x_pos-1][y_pos]
    if isvalid(x_pos-1, y_pos-1, grid):
        cnt+=grid[x_pos-1][y_pos-1]
    return cnt


def isvalid(i,j,grid):
    """
    Check if the given coordinates (i, j) are within the bounds of the grid.

    Parameters:
    i (int): The row index to check.
    j (int): The column index to check.
    grid (list of lists): The 2D grid in which to check the coordinates.

    Returns:
    bool: True if the coordinates (i, j) are valid
    (i.e., within the bounds of the grid), False otherwise.
    """
    if(0<= i < len(grid) and 0<= j < len(grid[i])):
        return True
    return False





def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    dim = int(input())

    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            sum_val = int(input())

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break


if __name__ == "__main__":
    main()
