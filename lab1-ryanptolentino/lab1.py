def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError  # raises error if list is None
    if len(int_list) == 0:
        return None
    highest = int_list[0]  # placeholder for highest known number
    for num in int_list:
        if num > highest:  # checks if any number is greater than the highest know number
            highest = num  # sets new highest known number
    return highest


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    if len(int_list) == 0:
        return []
    result = [int_list[-1]] + reverse_rec(int_list[:-1])  # creates a new list that can be added to on next func call
    return result


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
    if int_list is None:
        raise ValueError
    if len(int_list) == 0:
        return None
    if low <= high:
        mid = (high+low)//2
        if int_list[mid] == target:  # if target is at center
            return mid
        elif target < int_list[mid]:  # lower bound
            return bin_search(target, low, mid-1, int_list)
        else:  # higher bound
            return bin_search(target, mid+1, high, int_list)
    else:  # if target not found
        return None


def reverse_list_mutate(int_list):
    '''Reverses a list, mutates the input list, returns None
   If list is None, raises ValueError'''
    if int_list is None:
        raise ValueError
    if len(int_list) == 0:
        return None
    length = len(int_list)
    og_list = tuple(int_list)  # converted to tuple so doesn't change throughout and can be referenced
    for i in range(length):
        int_list[i] = og_list[length - 1 - i]  # Change values to their reverse indexes
    return None
