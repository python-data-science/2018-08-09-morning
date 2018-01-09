"""
Run:
    python -m doctest -v exercise.py
"""

# problem 1
# ------------------------------------------------------------------- #
people = ['Bob Smith', 'Ken Jones', 'Alex Bradino']


def sort_by_last_name(people):
    """
    Sort by last names

    Agruments: First Last names
    Returns: sorted list of names by last name

    Doctests:
        >>> sort_by_last_name(['Bob Smith', 'Ken Jones', 'Alex Bradino'])
        ['Alex Bradino', 'Ken Jones', 'Bob Smith']
    """
    return sorted(people, key=lambda x: x.rsplit(None,1)[-1])


# problem 2
# ------------------------------------------------------------------- #

names = ['James', 'Susan', 'Maggie']
ages = [4, 9, 12]
d = {}

def create_dictionary_from_lists(names, ages):
    """
    Create dictionary from lists

    Agruments: names = list of names; ages = list of ages
    Returns: Dictionary of name and age

    Doctests:
        >>> create_dictionary_from_lists(['James', 'Susan', 'Maggie'], [4,9,12])
        {'James': 4, 'Susan': 9, 'Maggie': 12}
    """
    for k, v in zip(names, ages):
        d[k] = v
    return d




# problem 3
# ------------------------------------------------------------------- #

numbers = [5, 6, 7, 8, 9, 10, 11, 12]


def square_even_values_and_sum_under_10(numbers):
    """
        Squares even values under 10

        Agruments: numbers
        Returns: sum of even squares

        Doctests:
        >>> square_even_values_and_sum_under_10([5, 6, 7, 8, 9, 10, 11, 12])
        344
    """
    evens = list(filter(lambda n: n % 2 == 0 , numbers))
    return sum(list(map(lambda n: n**2, evens)))
