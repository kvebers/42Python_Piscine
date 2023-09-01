from typing import Any


def calculateMedian(list: list):
    list.sort()
    median = 0
    if (len(list) % 2 == 1):
        median = list[len(list) // 2 + 1]
    print(median)


def calculateQuartile(list: list):
    list.sort()
    median = 0
    print(median)


def calculateMean(list: list):
    print(sum(list) / len(list))


def calculateVar(list: list):
    print(sum(list) / len(list))


def calculateStd(list: list):
    print(sum(list) / len(list))


def ft_statistics(*args: Any, **kwargs: Any) -> None:
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
