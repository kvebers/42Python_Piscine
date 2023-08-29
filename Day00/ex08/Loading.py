import sys


"""
Takes the elements itterates trought the list of elements
numbers is static in C, 
yield return value that is continiusly modified
"""


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for number, elem in enumerate(lst, 1):
        progress = int(number / total * 100)
        bar = "▓" * progress + "|" + " " * (100 - progress)
        if progress == 100:
            bar = "▓" * progress
        print(f"{progress}% |{bar}| {number}/{total}  \r", end = '', flush=True, file=sys.stderr)
        yield elem
