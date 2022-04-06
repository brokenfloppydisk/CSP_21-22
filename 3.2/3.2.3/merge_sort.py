comparisons = 0

def merge_sort(arr):
    """ Merge Sort
        Complexity: O(n log(n))
    """
    # Our recursive base case
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left= merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):
    """ Merge helper
        Complexity: O(n)
    """

    global comparisons

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        comparisons += 1
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    # Add the left overs if there's any left to the result
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        comparisons += 1
    # Add the left overs if there's any left to the result
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]
        comparisons += 1

    # Return result
    return merged

if __name__ == "__main__":
    array = [12, 5, 11, 6, -3, -4, -11, 6, 3, 4, 1, -2]
    doubled_array = array.copy() + [-8, 15, 25, -2, 0, 3, -4, 27, 13, 15, 10, 8]
    quadrupled_array = doubled_array.copy() + doubled_array.copy()
    
    array = merge_sort(array)
    print(array)
    print(comparisons)

    comparisons = 0
    doubled_array = merge_sort(doubled_array)
    print(doubled_array)
    print(comparisons)

    comparisons = 0
    quadrupled_array = merge_sort(quadrupled_array)
    print(quadrupled_array)
    print(comparisons)