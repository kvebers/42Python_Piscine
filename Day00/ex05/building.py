import sys


def main():
    """
    1. Chars in Text totalChars
    2. Lower Cases in Text lowerCase = 0
    3. upperCase = 0
    4. Punctuation in the text puncts = 0
    5. Spaces in the text spaces = 0
    6. Digits in the text digits = 0
    """
    totalChars = 0
    lowerCase = 0
    upperCase = 0
    puncts = 0
    spaces = 0
    digits = 0
    text = ""
    if len(sys.argv) > 2:
        raise AssertionError(" incorrect ammount of arguments")
        return 1
    elif len(sys.argv) == 1:
        try:
            text = input("Your input here?\n")
            text += "\n"
        except EOFError:
            pass
    else:
        text = sys.argv[1]

    for char in text:
        totalChars += 1
        if char.isdigit():
            digits += 1
        elif char == " " or char == "   " or char == "\n":
            spaces += 1
        elif char.isalpha() and char.isupper():
            upperCase += 1
        elif char.isalpha():
            lowerCase += 1
        else:
            puncts += 1
    print(f"The text contains {totalChars} characters:")
    print(f"upper case: {upperCase}")
    print(f"lower case: {lowerCase}")
    print(f"punctuation: {puncts}")
    print(f"spaces: {spaces}")
    print(f"digits: {digits}")


if __name__ == "__main__":
    """
    Tries to execute the main on error exits with error message
    """
    try:
        exit(main())
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
