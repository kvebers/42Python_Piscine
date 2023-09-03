from typing import Any


def mySum(list: list):
    """MY SUM"""
    sum = 0
    for amazing in list:
        sum += amazing
    return sum


def mySort(list):
    """MySort"""
    for amazing in range(myLen(list) - 1):
        for sure in range(myLen(list) - amazing - 1):
            if list[sure] > list[sure + 1]:
                list[sure], list[sure + 1] = list[sure + 1], list[sure]
    return list


def myLen(list: list):
    """My Length Function"""
    cnt = 0
    for amazing in list:
        cnt += 1
    return cnt


def calculateMedian(list: list):
    """Calculates the medium value"""
    list = mySort(list)
    median = 0
    if (myLen(list) % 2 == 1):
        median = list[myLen(list) // 2 + 1]
    else:
        median = (list[myLen(list) // 2] + list[myLen(list) // 2 - 1]) / 2
    print(median)


def calculateQuartile(list: list):
    """Calculates the 25% and 75% value"""
    list = mySort(list)
    newList = []
    leng = myLen(list)
    Q1Index = (leng - 1) // 4
    if leng % 4 == 0:
        q1 = (list[Q1Index] + list[Q1Index + 1]) / 2
    else:
        q1 = list[Q1Index]
    Q3Index = (3 * (leng - 1)) // 4
    if leng % 4 == 0:
        q3 = (list[Q3Index] + list[Q3Index + 1]) / 2
    else:
        q3 = list[Q3Index]
    newList = [q1, q3]
    print(newList)


def calculateMean(list: list):
    """Calculates the average value"""
    print(mySum(list) / myLen(list))


def calculateVar(list: list):
    """Calculates the average distance from mean"""
    mean = mySum(list) / myLen(list)
    var = 0
    for x in list:
        var += (x - mean) ** 2
    var = var / myLen(list)
    print(var)


def calculateStd(list: list):
    """Calculates the disperity of the data"""
    mean = mySum(list) / myLen(list)
    var = 0
    for x in list:
        var += (x - mean) ** 2
    var = var / myLen(list)
    std = var ** (0.5)
    print(std)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Loops trought 2 lists
        Args list takes only int and float
        kwargs list takes only keys and string
        Then it dose appropriate calculatins
        depending from the functions selected"""
    try:
        list = []
        median = 0
        mean = 0
        quartile = 0
        std = 0
        var = 0
        list = [var for var in args if type(var).__name__ == "int"
                or type(var).__name__ == "float"]
        for key, args in kwargs.items():
            if (args == "median"):
                median = 1
            elif (args == "mean"):
                mean = 1
            elif (args == "quartile"):
                quartile = 1
            elif (args == "std"):
                std = 1
            elif (args == "var"):
                var = 1
        if (myLen(list) == 0):
            if (median == 1):
                print("ERROR")
            if (mean == 1):
                print("ERROR")
            if (quartile == 1):
                print("ERROR")
            if (std == 1):
                print("ERROR")
            if (var == 1):
                print("ERROR")
            return
        if (median == 1):
            calculateMedian(list)
        if (quartile == 1):
            calculateQuartile(list)
        if (mean == 1):
            calculateMean(list)
        if (std == 1):
            calculateStd(list)
        if (var == 1):
            calculateVar(list)
    except Exception as e:
        print(f"An error occurred: {e}")
