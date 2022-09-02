def out_of_bounds(location, limit1, limit2=None):
    '''
    :param location: tuple representing location
    :param limit1: tuple representing upper limit if limit2 not present otherwise lower limit
    :param limit2: tuple representing upper limit if present else None
    :return: if the location is out of the bounds or not
    '''
    if len(location) != len(limit1):
        return True
    
    if limit2:
        for i in range(len(limit1)):
            if limit1[i] <= location[i] < limit2[i]:
                continue
            else:
                return True
    else:
        for i in range(len(limit1)):
            if 0 <= location[i] < limit1[i]:
                continue
            else:
                return True

    return False

def threshold(nums, limit, lower=True):
    '''
    :param nums: list or tuple of numbers to check
    :param limit: threshold to check numbers against
    :param lower: whether the numbers should be above or below the limit
    :return: if every number is above/below the given threshold
    '''
    for i in nums:
        if lower and 0 <= i <= limit or not lower and i >= limit:
            continue
        else:
            return False
    
    return True

def compare(num, limit):
    '''
    :param num: number to compare with
    :param limit: limit to compare against
    :return: 0 if neither, 1 if higher, -1 if lower than limit
    '''
    if num > limit:
        return 1
    if num < limit:
        return -1
    else:
        return 0

def compare_list(nums, limits):
    '''
    :param nums: list of numbers to compare with
    :param limits: int or list of limits to compare against
    :return: list of 1, -1, or 0 if greater, less than, or neither respectively
    '''
    if type(limits) == int:
        limits = [limits for _ in range(len(nums))]

    return [compare(i, j) for i, j in zip(nums, limits)]