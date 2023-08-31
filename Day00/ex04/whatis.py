import sys


def main():
    if len(sys.argv) != 2:
        raise AssertionError(" Incorrect Argument Count")
        return 1
    input_value = sys.argv[1]
    try:
        input_int = int(input_value)
    except ValueError:
        raise AssertionError(" argument is not an integer")
        return 1
    if input_int % 2 == 0:
        print("I am Even")
    else:
        print("I am Odd")
    return 0


if __name__ == "__main__":
    try:
        exit(main())
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
