def out_of_bounds(location, limit1, limit2=None):
    '''
    :param location: tuple representing location
    :param limit1: tuple representing upper limit of limit2 not present otherwise lower limit
    :param limit2: tuple representing upper limit if present else None
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