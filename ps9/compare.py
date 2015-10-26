import sys
import itertools

def valid_perms1(blocks):
    """
    valid_perms takes a list of blocks
    and returns all valid permutations
    of the blocks (in which length <= width)

    inputs:
    1. lst (a list of list of format [l, w, h])

    outputs:
    1. valid_perms_lst (a list of lists of format [l, w, h])
    """

    # accumulator for valid perms
    valid_perms_lst = []

    # for every block size
    for block in blocks:

        # generate all possible permutations
        permutations = perms(block)

        # from within all the possible permutations,
        # select the valid subset for which length <= width
        for perm in permutations:
            if perm[0] <= perm[1] and perm not in valid_perms_lst:
                valid_perms_lst.append(perm)

    return valid_perms_lst


def perms(block):
    """
    perms takes a single block and
    returns all permutations of that block

    inputs:
    1. block (a list of lists of format [l, w, h])

    outputs:
    1. result (a list of lists of format [l, w, h]),
    all permutations of block
    """

    # base case: the only permutation of a single
    # element is itself
    if len(block) == 1:
        return [block]

    # recursive case:
    result = []

    # take the first element
    first = block[0]

    # permutations of the list w/o the first element
    rest = perms(block[1:])

    # insert the first element into every index spot
    # of every permutation of the rest of the list
    for perm in rest:
        length = len(perm)
        for i in range(0, length+1):
            result.append(perm[0:i] + [first] + perm[i:])

    return result


def valid_perms2(blocks):
    """
    valid_perms takes a list of blocks
    and returns all valid permutations
    of the blocks (in which length <= width)

    inputs:
    1. lst (a list of list of format [l, w, h])

    outputs:
    1. valid_perms_lst (a list of lists of format [l, w, h])
    """

    # accumulator for valid perms
    valid_perms_lst = []

    # for every block size
    for block in blocks:

        # generate all possible permutations
        permutations = list(itertools.permutations(block))

        # from within all the possible permutations,
        # select the valid subset for which length <= width
        for perm in permutations:
            if perm[0] <= perm[1] and perm not in valid_perms_lst:
                valid_perms_lst.append(perm)

    return valid_perms_lst




def parse_input_file(path):
    """
    parse_input_file takes the path to a file
    and extracts the block information from that file,
    in [l, w, h] format

    inputs:
    1. path (a string; the path to the file)

    outputs:
    1. block_types (a list of lists of format [l, w, h]),
    the list of block types
    """

    block_types = []

    # open the file
    with open(path, 'r') as input_file:
        input_list = input_file.readlines()

        # ignore the first argument, which is the number of blocks
        for index, value in enumerate(input_list[1:]):

            # remove new lines
            block_types.append(value.replace("\n", "").split(" "))

            # extract length, width, and height
            l = int(block_types[index][0])
            w = int(block_types[index][1])
            h = int(block_types[index][2])

            # add a list of [l, w, h]
            block_types[index] = [l, w, h]

    return block_types





# read in input and output files
infile = sys.argv[1]
outfile = sys.argv[2]

# get the block sizes and their valid permutations
block_types = parse_input_file(infile)
block_perms = valid_perms1(block_types)
block_perms2 = valid_perms2(block_types)

print block_perms
print "------------------"
print block_perms2

