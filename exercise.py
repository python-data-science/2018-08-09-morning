# problem 1
# ------------------------------------------------------------------- #
people = ['Bob Smith', 'Ken Jones', 'Alex Bradino']


def sort_by_last_name(people, order='ASC'):
    # return full names sorted by last name in either ascending or descending order
    # add doctests make sure it passes
    """
    Arguments: List of name strings, string 'ASC'(default) or 'DESC'
    Return: List of name strings sorted by last name according to asc/desc order input
    >>> sort_by_last_name(['Bob Smith', 'Ken Jones', 'Alex Bradino'])
    ['Alex Bradino', 'Ken Jones', 'Bob Smith']
    >>> sort_by_last_name(['Ken Jones', 'Bob Smith', 'Alex Bradino'],'DESC')
    ['Bob Smith', 'Ken Jones', 'Alex Bradino']
    """
    if order == 'DESC':
        return sorted(sorted(people),key=lambda n: n.split(' ')[-1], reverse=True)
    else:
        return sorted(sorted(people),key=lambda n: n.split(' ')[1])


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
    return dict(zip(names, ages))


# problem 3
# ------------------------------------------------------------------- #
numbers = [5, 6, 7, 8, 9, 10, 11, 12]


def square_even_values_and_sum_under_10(numbers):
    # [6^2 + 8^2]
    # add doctests make sure it passes
    """
    >>> square_even_values_and_sum_under_10([5, 6, 7, 8, 9, 10, 11, 12])
    100
    """
    return sum([x**2 for x in filter(lambda n: (n < 10 and n%2 == 0), numbers)])

