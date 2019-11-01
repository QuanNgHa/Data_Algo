

def maxHeapify(A, n, i):
    # To heapify subtree rooted at index i.
    l = 2*i + 1 #in Python: root starts at index = 0 => Left will be (2i + 1)
    r = 2*i + 2 

    if (l < n and A[l] > A[i]):
        largest = l
    else:
        largest = i

    if (r < n and A[r]> A[largest]):
        largest = r
    
    if (largest != i):
        A[i], A[largest] = A[largest], A[i] # swap 
        maxHeapify(A, n, largest)

def buildMaxHeap(A,n):
    #Since from n//2 + 1 to n are all leaves
    #maxHeapify: from n//2 to root= 0 
    for i in range (n//2, -1, -1): 
        maxHeapify(A,n,i)
    

def heapSort(A):
    n = len(A)
    
    #build Max Heap for A
    buildMaxHeap(A,n)

    #Swap root (i = 0) of Max Heap to the end of the Array (i = n-1)
    #Now, Discard A[n-1] from Max Heap => Chilren of root remains Max Heap except Root
    # => maxHeapify(root of MaxHeap with discard A[n-1])
    for i in range(n-1, -1, -1):
        A[0], A[i] = A[i], A[0]
        maxHeapify(A, i, 0)

    return A


#print(heapSort([27,17,3,16,13,10,1,5,7,12,4,8,9,0]))
print(heapSort([5,13,2,25,7,17,20,8,4]))


