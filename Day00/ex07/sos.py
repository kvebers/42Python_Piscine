import sys


"""
WOW JUST COULD HAVE IMPORTED MORSE CODE I LOVE THESE RULES...
"""

NESTED_CODE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}


def main():
    if (len(sys.argv) != 2):
        raise AssertionError(" Incorrect ammount of arguments")

    code = []
    for char in sys.argv[1].upper():
        if (char in NESTED_CODE):
            code.append(NESTED_CODE[char])
        else:
            raise AssertionError(f" This bad boy char is invalid {char}")
    """
    joins the list elements into a string elemenets
    """
    print("".join(code))
    return (0)


if __name__ == "__main__":
    """
    Tries to execute the main on error exits with error message
    """
    try:
        exit(main())
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
