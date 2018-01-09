# problem 1
# ------------------------------------------------------------------- #
people = ['Bob Smith', 'Ken Jones', 'Alex Bradino']


def sort_by_last_name(people, order):
    # return full names sorted by last name in either ascending or descending order
    # add doctests make sure it passes
    """
    arguments:
    Order = True if you want to sort descending; False if you want to sort ascending

    >>> sort_by_last_name(people, True)
    ['Bob Smith', 'Ken Jones', 'Alex Bradino']
    """

    return sorted(people, key=lambda x: x.split()[1], reverse=order)

# problem 2
# ------------------------------------------------------------------- #
names = ['James', 'Susan', 'Maggie']
ages = [4, 9, 12]


def create_dictionary_from_lists(names, ages):
    # {'James':4, 'Susan':9, 'Maggie':12}
    # add doctests make sure it passes
    """
    >>> create_dictionary_from_lists(names, ages)
    {'James': 4, 'Susan': 9, 'Maggie': 12}
    """
    return dict(zip(names,ages))

# problem 3
# ------------------------------------------------------------------- #
numbers = [5, 6, 7, 8, 9, 10, 11, 12]


def square_even_values_and_sum_under_10(numbers):
    # 6^2 + 8^2]
    # add doctests make sure it passes
    """
    >>> square_even_values_and_sum_under_10(numbers)
    100
    """
    b=[n**2 for n in numbers if n%2==0 and n<10]
    return sum(b)
