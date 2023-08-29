def slice_me(family: list, start: int, end: int) -> list:
    try:
        if (len(family) == 0):
            print("My shape is : (0, 0)")
            print("My new shape is : (0, 0)")
            return family
        if (type(family) is not list or type(start) \
        is not int or type(end) is not int):
            raise AssertionError("Check of the parameters in the list")
        leng = len(family[0])
        for each in family:
            if (len(each) != leng):
                raise AssertionError("The list in inccorectly formated")
        if (end < 0):
            end = len(family) + end
        if (end < start):
            raise AssertionError("Incorrect end values")
        print(f"My shape is : ({len(family)}, {len(family[0])})")
        newFamily = family[start:end]
        print(f"My shape is : ({len(newFamily)}, {len(newFamily[0])})")
        return newFamily
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    return
