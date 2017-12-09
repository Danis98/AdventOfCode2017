seq = open('day9.input').read().rstrip()

nest_level = 0
in_garbage = False
index = 0
total = 0
garbage_count = 0

while index < len(seq):
    if in_garbage:
        garbage_count += 1
    if seq[index] == '{' and not in_garbage:
        nest_level += 1
        total += nest_level
    elif seq[index] == '}' and not in_garbage:
        nest_level -= 1
    elif seq[index] == '<':
        in_garbage = True
    elif seq[index] == '>':
        in_garbage = False
        garbage_count -= 1
    elif seq[index] == '!':
        index += 1
        garbage_count -= 1
    index += 1

print garbage_count
