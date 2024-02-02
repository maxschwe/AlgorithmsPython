import random
import time

def insertion_sort(array):
    for i in range(1, len(array)):
        x = array[i]
        while x < array[i - 1] and i > 0:
            array[i] = array[i - 1]
            i -= 1
        array[i] = x
        print(f"{array=}")

    
if __name__ == "__main__":
    random.seed(time.time())
    array = list(range(10))
    random.shuffle(array)

    insertion_sort(array)
    print(f"{array=}")
