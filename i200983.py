"""
    function to find nth fibonacci number
    """
def fib_num(index):
    """
    function to find nth fibonacci number
    """
    i_one = 0
    i_two = 1
    if index == 1:
        return i_one
    elif index == 2:
        return i_two
    else:
        count = 2
        while count != index:
            temp = i_two
            i_two = i_two + i_one
            i_one = temp
        return i_two
    