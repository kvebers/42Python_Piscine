import string


def main():
    totalChars = 0
    lowerCase = 0
    upperCase = 0
    puncts = 0
    spaces = 0
    digits = 0
    text = input("Input Text: ")

    for char in text:
        totalChars += 1
        if char.isdigit():
            digits += 1
        elif char == " ":
            spaces += 1
        elif char.isalpha() and char.isupper():
            upperCase += 1
        elif char.isalpha():
            lowerCase += 1
        elif char in string.punctuation or char == "-":
            puncts += 1
    print(f"The text contains {totalChars} characters:")
    print(f"upper case: {upperCase}")
    print(f"lower case: {lowerCase}")
    print(f"punctuation: {puncts}")
    print(f"spaces: {spaces}")
    print(f"digits: {digits}")


if __name__ == "__main__":
    main()
