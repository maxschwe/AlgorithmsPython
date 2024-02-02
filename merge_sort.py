import random
import time


def merge(array, start, middle, end):
    print(f"{array}, {start}:{middle}:{end}")
    temp_array = [0 for _ in range(end - start)]
    for i in range(middle - start):
        temp_array[i] = array[i + start]
    for j in range(end - 1, middle - 1, -1):
        i += 1
        temp_array[i] = array[j]
        
    index_left = 0
    index_right = end - start - 1
    for i in range(start, end):
        if temp_array[index_left] < temp_array[index_right]:
            array[i] = temp_array[index_left]
            index_left += 1
        else:
            array[i] = temp_array[index_right]
            index_right -= 1 

def merge_sort_subset(array, start, end):
    if end - start <= 1:
        return
    middle = (end - start) // 2 + start
    merge_sort_subset(array, start, middle)
    merge_sort_subset(array, middle, end)
    merge(array, start, middle, end) 

def merge_sort(array):
    merge_sort_subset(array, 0, len(array))

if __name__ == "__main__":
    random.seed(time.time())
    array = list(range(16))
    random.shuffle(array)

    merge_sort(array)
    print(f"{array=}")