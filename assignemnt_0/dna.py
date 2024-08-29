"""
DNA
"""

# File:dna.py
# Description:
# Student Name: Tanner Jackson
# Student EID: twj393
# Partner Name: Shanmukha Pinapati
# Partner UT EID : ssp3428
# Course Name : CS 313E
# Unique Number : 50183
# Date Created : 8/28/24
# Date Last Modified: 8/28/24
# Input: S1 and S2 are two Strings of DNA
# Output: Return the longest subtring of DNA between each pair of strands


def longest_subsequence(string_1, string_2):
    return string_1 + string_2
#Used to check for longest subsequence between (string_1) and (string_2)





def main():
    """
    This main function reads the data input files and
    prints to the standard output. 
    NO NEED TO CHANGE THE MAIN FUNCTION.
    """
    # read the data
    # number of lines
    n_lines = int(input())

    # for each pair
    for _ in range(0, n_lines):
        str_1 = input()
        str_2 = input()

        # call longest_subsequence
        subsequences = longest_subsequence(str_1, str_2)

        # write out result(s)
        if not subsequences:
            print("No Common Sequence Found")

        for subsequence in subsequences:
            print(f"{subsequence}")

        # insert blank line
        print()


if __name__ == "__main__":
    main()
