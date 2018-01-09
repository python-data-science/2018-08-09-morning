# problem 1
# ------------------------------------------------------------------- #
people = ['Bob Smith', 'Ken Jones', 'Alex Bradino']


def sort_by_last_name(people, order):
    """
    Doctests:
        >>> sort_by_last_name(['Bob Smith', 'Ken Jones', 'Alex Bradino'], True)
        ['Smith, Bob', 'Jones, Ken', 'Bradino, Alex']
    """
    # return full names sorted by last name in either ascending or descending order
    # add doctests make sure it passes
    return sorted([n.split(" ")[1] +", " + n.split(" ")[0] for n in people], reverse = order)


# problem 2
# ------------------------------------------------------------------- #
names = ['James', 'Susan', 'Maggie']
ages = [4, 9, 12]


def create_dictionary_from_lists(names, ages):
    """
    Doctests:
        >>> create_dictionary_from_lists(['James', 'Susan', 'Maggie'], [4, 9, 12])
        {'James': 4, 'Susan': 9, 'Maggie': 12}
    """
    # {'James':4, 'Susan':9, 'Maggie':12}
    # add doctests make sure it passes
    return {n:a for n, a in zip(names, ages)}

# problem 3
# ------------------------------------------------------------------- #
numbers = [5, 6, 7, 8, 9, 10, 11, 12]


def square_even_values_and_sum_under_10(numbers):
    """
    Argument: List of numbers
    Return int
    Doctests:
        >>> square_even_values_and_sum_under_10([5, 6, 7, 8, 9, 10, 11, 12])
        100
    """
    # 6^2 + 8^2]
    # add doctests make sure it passes
    return sum([n**2 for n in numbers if n % 2 == 0 and n < 10])
