import random
import time


def partition(array, start, end, splitter_index):
    splitter_value = array[splitter_index]
    print(f"{array=}, {splitter_value}")
    array[splitter_index] = array[start]
    new_splitter_index = start
    for i in range(start+1, end):
        if array[i] < splitter_value:
            new_splitter_index += 1
            array[new_splitter_index], array[i] = array[i], array[new_splitter_index]
    array[start] = array[new_splitter_index]
    array[new_splitter_index] = splitter_value

    return new_splitter_index


def quick_sort_subset(array, start, end):
    if (end - start) <= 1:
        return
    splitter_index = (end - start) // 2 + start
    new_splitter_index = partition(array, start, end, splitter_index)
    quick_sort_subset(array, start, new_splitter_index)
    quick_sort_subset(array, new_splitter_index + 1, end)
    

def quick_sort(array):
    quick_sort_subset(array, 0, len(array))

if __name__ == "__main__":
    random.seed(time.time())
    array = list(range(10))
    random.shuffle(array)

    quick_sort(array)
    print(f"{array=}")