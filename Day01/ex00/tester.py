from give_bmi import give_bmi, apply_limit


def main():
    """
    EXECUTES THE MAIN FUNCTUON
    """
    height = [5, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 25))


if __name__ == "__main__":
    exit(main())

