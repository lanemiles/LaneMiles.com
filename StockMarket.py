import sys
import math


def compute_longest_nondecreasing_sequence(lst):
    """
    Input: A list of tuples of the form (day #, price)

    Output: A tuple of:
            i. An integer representing the longest consecutive
                 non-decreasing sequence (LCS) of numbers in the list
            ii. An integer representing the day the sequence starts
            iii. A list of tuples of the form (day #, price) in
                representing the longest consecutive non-decreasing
                sequence (LCS) in increasing day order


    General Approach:
        1. The LCS is either completely contained in the left half
            of the array, completely contained in the right half
            of the array, or begins in the left half and ends in
            the right half.
        2. Thus, we can solve this problem in a divide and conquer
            manner by recursively solving it on the left and right
            halves and doing separate work to find split sequences.
    """

    # in the base case, array length is 1, so we return 1 and the values
    if len(lst) == 1:
        return (1, 1, [lst[0]])
    elif not lst:
        return (0, 0, [])

    # calculate left and right half indices
    left_half_index = int(math.floor(len(lst)/2))
    right_half_index = int(math.ceil(len(lst)/2))

    # find the LCS in each half, and the LCS in the split sequences
    max_left = compute_longest_nondecreasing_sequence(lst[:left_half_index])
    max_right = compute_longest_nondecreasing_sequence(lst[right_half_index:])
    max_split = compute_longest_split_sequence(lst)

    # find max LCS length and return relevant info
    return max(max_left, max_right, max_split, key=lambda item: item[0])


def compute_longest_split_sequence(lst):
    """
    Input: A list of tuples of the form (day #, price)

    Output: A tuple of:
            i. An integer representing the longest consecutive
                 non-decreasing sequence (LCS) of numbers in the list
                 where the sequence begins in the left half and ends in
                 the right half
            ii. An integer representing the day the sequence starts
            iii. A list of tuples of the form (day #, price) in
                representing the longest consecutive non-decreasing
                sequence (LCS) in increasing day order

    General Approach:
        1. Check if the first element in the right half is
            at least the last element in the left half.
                a. If so:
                    i.  Compute larest sequence that ends at
                        last element in left half
                    ii. Compute larest sequence that begins at
                        first element in right half
                    iii. Return sum(largest_left, largest_right)
                b. If not, return a sentinel (-1, -1, [])
    """

    # if less than 2 return bad times
    if len(lst) < 2:
        return (-1, [])

    # compute the left and right middle indices
    left_half_index = int(math.floor(len(lst)/2))
    right_half_index = int(math.ceil(len(lst)/2))

    # make the left and right halves
    left_half = lst[:left_half_index]
    right_half = lst[right_half_index:]

    # check if the first element in the right half is >= last in left
    if right_half[0][1] >= left_half[-1][1]:

        left_done = False
        left_last_val = sys.maxsize
        left_days = []

        # compute longest in left half ending at last element
        for idx, val in enumerate(reversed(left_half)):

            if val[1] <= left_last_val and not left_done:
                left_days.append(val)
                left_last_val = val[1]

            elif val[1] > left_last_val:
                left_done = True
                break

        # compute longest in rigth half starting at first
        right_done = False
        right_last_val = -1
        right_days = []

        # compute longest in right half beginning at first element
        for idx, val in enumerate(right_half):

            if val[1] >= right_last_val and not right_done:
                right_days.append(val)
                right_last_val = val[1]

            elif val[1] < right_last_val:
                right_done = True
                break

        max_lcs = list(reversed(left_days)) + right_days
        return (len(max_lcs), max_lcs[0][0], max_lcs)

    else:
        return (0, [])


# hold the args
arg_list = []

# we know arg 2 is the infile, arg 3 is the out file
for index, arg in enumerate(sys.argv):
    arg_list.append(arg)

# assign inputs
input_file_path = arg_list[1]
output_file_path = arg_list[2]

# read the input file into a list
input_file = open(input_file_path, "r")
input_nums = input_file.read().split('\n')

# remove a potential blank line at the end
input_nums = filter(None, input_nums)

# turn that into list of tuples of (day #, price)
input_list = list(enumerate(input_nums))

# convert all to ints
for day, price in input_list:
    input_list[day] = (day, int(price))

# remove the number of days
input_list = input_list[1:]

# compute compute longest nondecreasing sequence
lcs = compute_longest_nondecreasing_sequence(input_list)

# write this to the output
with open(output_file_path, "w") as output_file:

    # first line is max LCS length
    output_file.write(str(lcs[0])+"\n")

    # now write start day
    output_file.write(str(lcs[1])+"\n")

    # and now prices, 1 per line
    for price in lcs[2]:
        output_file.write(str(price[1])+"\n")
