from random import randint

mega_list = []
num_blocks = 1000
max_dim_size = 100

for i in range(0, num_blocks):
    one = randint(1, max_dim_size)
    two = randint(1, max_dim_size)
    three = randint(1, max_dim_size)
    mega_list.append([one, two, three])

with open('custom1.in', 'w') as output:
    output.write(str(len(mega_list)) + "\n")
    for type in mega_list:
        s = ""
        for dim in type:
            s += str(dim) + " "
        s = s[:-1]
        output.write(s + "\n")
