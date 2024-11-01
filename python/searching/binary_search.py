def binary_search(sequence, item):
    """
    Performs a binary search on a sorted sequence to find the given item.

    Preconditions:
    - The input sequence must be sorted in non-decreasing order.

    :param sequence: A sorted sequence.
    :param item: The element to search for in the sequence.
    :return: The index of the item if found, otherwise None.

    Time Complexity:
    - Average and Worst Case: O(log n), where n is the number of elements in the sequence.
      Note: The logarithm is base 2 since the search space is halved at each step.

    Space Complexity:
    - O(1), since the algorithm operates iteratively and uses a constant amount of additional memory.
    """
    begin_index = 0
    end_index = len(sequence) - 1 # -1 as we start from 0 and not from 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None

