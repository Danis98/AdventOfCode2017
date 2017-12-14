key = open('day14.input').read().rstrip()

def knot_hash(in_str):
    in_seq = [ord(ch) for ch in in_str]
    in_seq += [17, 31, 73, 47, 23]

    list_len = 256
    nums = range(0, list_len)

    index = 0
    skip = 0

    for round_num in range(0, 64):
        for l in in_seq:
            arr = (nums[index:index+l] if index+l<list_len else nums[index:list_len]+nums[:(index+l)%list_len])[::-1]
            for i in range(index, index+l):
                nums[i%list_len] = arr[i-index]
            index = (index+l+skip)%list_len
            skip += 1

    final_hash = ''.join(["%02x"%n for n in [reduce(lambda i, j: int(i) ^ int(j), nums[i*16:(i+1)*16]) for i in range(0, 16)]])

    return final_hash

used_squares = 0
for i in range(0, 128):
    row_hash=int(knot_hash("%s-%d" % (key, i)), 16)
    used_squares += bin(row_hash).count('1')
print used_squares
