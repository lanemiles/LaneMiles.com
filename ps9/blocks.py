import sys


def valid_perms(blocks):
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


def main():
    """
    parse_input_file takes the path to a file
    and extracts the block information from that file,
    in [l, w, h] format

    inputs:
    1. path to this file - command line arg, string
    2. infile - command line arg, string
    3. outfile - command line arg, string

    outputs:
    1. prints to the console the height and number
    of blocks in the tallest possible tower
    2. prints to the outfile the number and type
    of blocks in the tallest possible tower
    """

    # read in input and output files
    infile = sys.argv[1]
    outfile = sys.argv[2]

    # get the block sizes and their valid permutations
    block_types = parse_input_file(infile)
    block_perms = valid_perms(block_types)

    # sort the list of block permutations based on area
    block_perms.sort(key=lambda x: x[0] * x[1], reverse=True)

    # begin dynamic programming
    blocks = []
    path = []
    temp_height = []

    # base case
    blocks.append((block_perms[0][2], None))

    # fill in rest of table
    for i in range(1, len(block_perms)):

        # worst case, the tallest tower is just block permutation i
        temp_height.append((block_perms[i][2], None))

        i_length = block_perms[i][0]
        i_width = block_perms[i][1]

        # for all lesser blocks, if stackable, compute total height if stacked
        for q in range(0, i):

            # if we can put the ith block permutation on top of the qth
            q_length = block_perms[q][0]
            q_width = block_perms[q][1]
            if (i_length < q_length) and (i_width < q_width):
                temp_height.append((blocks[q][0] + block_perms[i][2], q))

        # pick the maximum total height

        max_height = max(temp_height, key=lambda x: x[0])
        temp_height = []
        blocks.append(max_height)

    # get the height of the tallest possible tower
    (max_tower_height, below_block_index) = max(blocks, key=lambda x: x[0])

    # get the top block's index in the dynamic programming table
    cur_block_index = blocks.index((max_tower_height, below_block_index))

    # build up the path, from top to bottom
    while cur_block_index is not None:

        path.append(cur_block_index)

        # follow the pointer to the next block down
        cur_block_index = blocks[cur_block_index][1]

    # print descriptive sentence
    print "The tallest tower has", len(path), "blocks and a height of", max_tower_height

    # print to output file
    with open(outfile, 'w') as output:

        # print number of blocks
        output.write(str(len(path)) + "\n")

        # print out blocks in path, from largest to smallest
        for x in reversed(path):
            to_print = ""
            for dim in block_perms[x]:
                to_print += str(dim) + " "
            to_print = to_print[:-1] + "\n"
            output.write(to_print)

main()
