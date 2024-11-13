def MergeSort(A):
    if len(A) > 1:
        B = A[:(len(A) // 2)]
        C = A[(len(A) // 2):]
        MergeSort(B)
        MergeSort(C)
        Merge(B, C, A)

def Merge(B, C, A):
    i, j, k = 0, 0, 0
    while (i < len(B) and j < len(C)):
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
    if i == len(B):
        A[k:] = C[j:]
    else:
        A[k:] = B[i:]