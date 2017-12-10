len_seq = [int(e) for e in open('day10.input').read().rstrip().split(',')]
list_len = 256

nums = range(0, list_len)

index = 0
skip = 0

for l in len_seq:
    arr = (nums[index:index+l] if index+l<list_len else nums[index:list_len]+nums[:(index+l)%list_len])[::-1]
    for i in range(index, index+l):
        nums[i%list_len] = arr[i-index]
    index = (index+l+skip)%list_len
    skip += 1

print nums[0]*nums[1]
