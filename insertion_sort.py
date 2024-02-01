def insertion_sort(array):
    for i in range(1, len(array)):
        x = array[i]
        while x < array[i - 1] and i > 0:
            array[i] = array[i - 1]
            i -= 1
        array[i] = x
        print(f"{array=}")

    
array = [5, 1, 9, 8, 3, 4, 0, 2, 7, 6]
insertion_sort(array)
print(array)
