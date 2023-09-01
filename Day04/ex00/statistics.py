from typing import Any


def calculateMedian(list: list):
    """Calculates the medium value"""
    list.sort()
    median = 0
    if (len(list) % 2 == 1):
        median = list[len(list) // 2 + 1]
    else:
        median = (list[len(list) // 2] + list[len(list) // 2 - 1]) / 2
    print(median)


def calculateQuartile(list: list):
    """Calculates the 25% and 75% value"""
    list.sort()
    newList = []
    leng = len(list)
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
    newList.append(q1)
    newList.append(q3)
    print(newList)


def calculateMean(list: list):
    """Calculates the average value"""
    print(sum(list) / len(list))


def calculateVar(list: list):
    """Calculates the average distance from mean"""
    mean = sum(list) / len(list)
    var = 0
    for x in list:
        var += (x - mean) ** 2
    var = var / len(list)
    print(var)


def calculateStd(list: list):
    """Calculates the disperity of the data"""
    mean = sum(list) / len(list)
    var = 0
    for x in list:
        var += (x - mean) ** 2
    var = var / len(list)
    std = var ** (0.5)
    print(std)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Loops trought 2 lists
        Args list takes only int and float
        kwargs list takes only keys and string
        Then it dose appropriate calculatins
        depending from the functions selected"""
    list = []
    median = 0
    mean = 0
    quartile = 0
    std = 0
    var = 0
    for var in args:
        if isinstance(var, (int, float)):
            list.append(var)
    for key, args in kwargs.items():
        if isinstance(key, str):
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
    if (len(list) == 0):
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
