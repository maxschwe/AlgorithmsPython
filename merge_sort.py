def merge(array, start, middle, end):
    temp_array = [0 for _ in range(end - start)]
    for i in range(middle - start):
        temp_array[i] = array[i + start]
    for j in range(end - 1, middle - 1, -1):
        i += 1
        temp_array[i] = array[j]
    print(f"{array=}")
        
    index_left = 0
    index_right = end - start - 1
    for i in range(start, end):
        if temp_array[index_left] < temp_array[index_right]:
            array[i] = temp_array[index_left]
            index_left += 1
        else:
            array[i] = temp_array[index_right]
            index_right -= 1 

def merge_sort_call(array, start, end):
    if end - start <= 1:
        return
    middle = (end - start) // 2 + start
    merge_sort_call(array, start, middle)
    merge_sort_call(array, middle, end)
    merge(array, start, middle, end) 

def merge_sort(array):
    merge_sort_call(array, 0, len(array))

array = [5, 1, 9, 8, 3, 4, 0, 2, 7, 6]
merge_sort(array)
print(array)