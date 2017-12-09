seq = open('day9.input').read().rstrip()

nest_level = 0
in_garbage = False
index = 0
total = 0

while index < len(seq):
    if seq[index] == '{' and not in_garbage:
        nest_level += 1
        total += nest_level
    elif seq[index] == '}' and not in_garbage:
        nest_level -= 1
    elif seq[index] == '<':
        in_garbage = True
    elif seq[index] == '>':
        in_garbage = False
    elif seq[index] == '!':
        index += 1
    index += 1

print total
