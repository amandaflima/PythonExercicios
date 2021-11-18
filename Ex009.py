

for num in range (1,16):
    tot = 0
    for c in range(1, 16):
        if num % c == 0:
            tot += 1
    if tot == 2:
        print(f'{num}primo')
    else:
        print(f'{num}NAO E PRIMO')