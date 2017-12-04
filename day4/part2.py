passphrases = open('day4.input').read().rstrip().split('\n')

valid_count = 0
for passphrase in passphrases:
    freq = {}
    valid_count += 1
    for word in passphrase.split():
        word = ''.join(sorted(word))
        if word in freq:
            valid_count -= 1
            break
        freq[word] = 1
print valid_count
