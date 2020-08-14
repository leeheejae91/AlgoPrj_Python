def solution(A,B):
    A.sort()
    B.sort(reverse=True)

    return sum([A[i] * B[i] for i in range(len(A))])


in_A = [1, 4, 2]
in_B = [5, 4, 4]


print solution(in_A,in_B)