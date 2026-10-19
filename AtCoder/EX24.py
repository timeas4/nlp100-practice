N = int(input())

count =0
while(N>0):
    if N.bit_count()%2 == 1:
        N -= 1
    else:
        N -= 2
    count += 1
print(count)


