from math import sqrt

lower = 108100
upper = lower + 17000

def is_prime(num):
    for i in xrange(2, int(sqrt(num)+.5)):
        if num % i == 0:
            return False
    return True

cnt = 0
for num in xrange(lower, upper+1, 17):
    if not is_prime(num):
        cnt += 1
print cnt
