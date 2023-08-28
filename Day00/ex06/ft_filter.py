"""
Construct a list from those elements of iterable for which function returns true.
"""
def ft_filter(function, iterable):
    return [item for item in iterable if function(item)]