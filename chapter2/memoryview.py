from array import array


def memory_view_operations():
    numbers = array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    memv_unsigned_cast = memv.cast('B')  # two complement unsigned implementations (look into it when you have the time)
    print(memv_unsigned_cast.tolist())

    # [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
    # Note change to numbers : a 4 in the most significant byte of a 2-byte unsigned
    # integer is 1024.
    memv_unsigned_cast[5] = 4

