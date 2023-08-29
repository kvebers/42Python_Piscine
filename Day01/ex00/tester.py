from give_bmi import give_bmi, apply_limit


"""
EXECUTES THE MAIN FUNCTUON 

"""

def main():
    height = [5, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

if __name__ == "__main__":
    try:
        exit(main())
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))