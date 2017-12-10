len_seq = [ord(e) for e in open('day10.input').read().rstrip()]
len_seq += [17, 31, 73, 47, 23]

list_len = 256
nums = range(0, list_len)

index = 0
skip = 0

def hash_round():
    global index, skip
    for l in len_seq:
        arr = (nums[index:index+l] if index+l<list_len else nums[index:list_len]+nums[:(index+l)%list_len])[::-1]
        for i in range(index, index+l):
            nums[i%list_len] = arr[i-index]
        index = (index+l+skip)%list_len
        skip += 1

for round_num in range(0, 64):
    hash_round()

final_hash = ''.join(["%02x"%n for n in [reduce(lambda i, j: int(i) ^ int(j), nums[i*16:(i+1)*16]) for i in range(0, 16)]])

print final_hash
