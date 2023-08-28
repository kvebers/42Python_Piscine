import sys
from ft_filter import ft_filter


def main():    
    if (len(sys.argv) != 3):
        raise AssertionError(" Wrong number of arguments")
    else:
        numb = int(sys.argv[2])
        split = sys.argv[1].split()
        result = ft_filter(lambda word: len(word) > numb, split)
        print(result)
    return 0


if __name__ == "__main__":
    """
    Tries to execute the main on error exits with error message
    """
    try:
        exit(main())
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))

    # print(filter.__doc__)