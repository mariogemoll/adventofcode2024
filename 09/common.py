def checksum(fs):
    sum = 0
    for pos in range(len(fs)):
        if fs[pos] != '.':
            sum += pos * fs[pos]
    return sum
