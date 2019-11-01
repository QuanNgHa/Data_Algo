

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] < x:
            i+=1
            A[i], A[j] = A[j], A[i] #swap
    A[i+1], A[r] = A[r], A[i+1]
    return i+1



def quickSort(A, p, r):
    if p < r:
        q = partition(A,p,r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
    return A

A = [13,19,9,5,12,8,7,4,21,2,6,11]
r = len(A)
print(quickSort(A, 0, r-1))
    