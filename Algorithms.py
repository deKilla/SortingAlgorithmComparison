

def merge_sort(arr):
    # Split the list
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i = i+1
            else:
                arr[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j = j+1
            k = k+1


def insertion_sort(arr):
    for slot in range(1, len(arr)):
        value = arr[slot]
        test_slot = slot - 1
        while test_slot > -1 and arr[test_slot] > value:
            arr[test_slot + 1] = arr[test_slot]
            test_slot = test_slot - 1
        arr[test_slot + 1] = value
    return arr


def bubble_sort(arr):
    index = len(arr) - 1
    while index >= 0:
        for j in range(index):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        index -= 1
    return arr


def quick_sort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) > 1:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        arr = less + pivotList + more
    return arr


def max_heapify(A, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and A[left] > A[largest]:
        largest = left
    if right < heap_size and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, heap_size, largest)

def build_heap(A):
    heap_size = len(A)
    for i in range((heap_size//2),-1,-1):
        max_heapify(A,heap_size, i)

def heap_sort(arr):
    heap_size = len(arr)
    build_heap(arr)
    #print A #uncomment this print to see the heap it builds
    for i in range(heap_size-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(arr, heap_size, 0)


#testarr = [8,7,6,5,4,3,2,1]
#heap_sort(testarr)
#print(testarr)



