def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def insertionsort(array):
    comparisons = 0
    for i in range(0, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            swap(array, j-1, j)
            j -= 1
            comparisons += 1
    return comparisons

if __name__ == "__main__":
    array = [12, 5, 11, 6, -3, -4, -11, 6, 3, 4, 1, -2]
    doubled_array = array.copy() + [-8, 15, 25, -2, 0, 3, -4, 27, 13, 15, 10, 8]
    quadrupled_array = doubled_array.copy() + doubled_array.copy()

    print(insertionsort(array))
    print(array)

    print(insertionsort(doubled_array))
    print(doubled_array)

    print(insertionsort(quadrupled_array))
    print(quadrupled_array)