"""
    function to find nth fibonacci number
    """
def fib_num(index):
    """
    function to find nth fibonacci number
    """
    i1 = 0
    i2 = 1
    if index == 1:
        return i1
    elif index == 2:
        return i2
    else:
        count = 2
        while count != index:
            temp = i2
            i2 = i2 + i1
            i1 = temp
        return i2