from array2D import slice_me

def main():
    family = [[1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]]

    test = []

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
    # print(slice_me(family, 1, -8))
    # print(slice_me(test, 1, -8))

if __name__ == "__main__":
    try:
        exit(main())
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))