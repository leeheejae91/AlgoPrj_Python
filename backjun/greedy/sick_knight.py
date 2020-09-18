arr = str(input()).split()
N, M = [int(i) for i in arr]

if N >= 3 and M >= 7:
    print(M-2)
elif N >= 3 or M >= 7:
    if N >= 3:
        if M <= 4:
            print(M)
        elif M > 4:
            print(4)
    elif M >= 7:
        if N == 2:
            print(4)
        elif N == 1:
            print(1)
else:
    if N == 1:
        print(1)
    else:
        print(int((M-1)/2) + 1)

