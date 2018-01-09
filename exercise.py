# problem 1
# ------------------------------------------------------------------- #
def sort_by_last_name(people):
    # return full names sorted by last name in either ascending or descending order
    # add doctests make sure it passes
    """ Test sort_by_last_name

    Args:
        people : the first parameter
        order : the second parameter
    Returns:
        x : return value
        y : return value 2
    >>> sort_by_last_name(['Bob Smith', 'Ken Jones', 'Alex Bradino'])
        ['Alex Bradino', 'Ken Jones','Bob Smith']
    """
    x = sorted(people, key=lambda name: name.split(" ")[-1])
    return (x)
    pass


# problem 2
# ------------------------------------------------------------------- #
def create_dictionary_from_lists(names, ages):
    # {'James':4, 'Susan':9, 'Maggie':12}
    # add doctests make sure it passes
    """ Test create_dictionary_from_lists

    Args:
        names : the first parameter
        ages : the second parameter
    Returns:
        new_dict : return value
    >>> create_dictionary_from_lists(['James', 'Susan', 'Maggie'],[4, 9, 12])
        {'James': 4, 'Susan': 9, 'Maggie': 12}
    """
    new_dict = dict(zip(names, ages))
    return (new_dict)
    pass


# problem 3
# ------------------------------------------------------------------- #

def square_even_values_and_sum_under_10(numbers):
    # 6^2 + 8^2]
    # add doctests make sure it passes
    """ Test square of evens

    Args:
        numbers : the first parameter

    Returns:
        squares : return value
    >>> square_even_values_and_sum_under_10([5, 6, 7, 8, 9, 10, 11, 12])
        100
    """
    l1 = filter(lambda n: n < 10, numbers))
    sum = 0
    for i in l1:
        if i % 2 == 0:
        sum = sum + (i*i)
        return (sum)
    pass
