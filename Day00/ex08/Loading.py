import sys


def ft_tqdm(lst: range) -> None:
    """
    Takes the elements iterates through the list of elements.
    Numbers are static in C.
    Yields a continuously modified return value.
    """
    total = len(lst)
    for number, elem in enumerate(lst, 1):
        progress = int(number / total * 100)
        bar = "▓" * progress + "|" + " " * (100 - progress)
        if progress == 100:
            bar = "▓" * progress
        print(f"{progress}% |{bar}| {number}/{total}\r",
              end='', flush=True, file=sys.stderr)
        yield elem
