import random
import time

def sift_down(array, i, end):
    while True:
        index_larger_child = i * 2 + 1 # initially set left child as larger child 
        if index_larger_child >= end:
            # node has not a left child
            break
        index_right_child = index_larger_child + 1
        if index_right_child < end and array[index_right_child] > array[index_larger_child]:
            # node has a right child and it has a larger value than left child
            index_larger_child = index_right_child
        
        if array[index_larger_child] > array[i]:
            array[i], array[index_larger_child] = array[index_larger_child], array[i]
            i = index_larger_child
        else:
            break
    

def heapify(array):
    len_array = len(array)
    for i in range(len_array // 2 - 1, -1, -1):
        sift_down(array, i, len_array)

def heap_sort(array):
    heapify(array)
    for j in range(len(array) - 1, 0, -1):
        print(f"{array=}")
        array[0], array[j] = array[j], array[0]
        sift_down(array, 0, j)

if __name__ == "__main__":
    random.seed(time.time())
    array = list(range(10))
    random.shuffle(array)

    heap_sort(array)
    print(f"{array=}")