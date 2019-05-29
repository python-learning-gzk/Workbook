with open('1.txt') as f:
    print sum(len(line.split()) for line in f)