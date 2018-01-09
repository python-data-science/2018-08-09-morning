"""
Run:
    python -m doctest -v exercise.py
"""

# problem 1
# ------------------------------------------------------------------- #
people = ['Bob Smith', 'Ken Jones', 'Alex Bradino']


def sort_by_last_name(people, order):
    # return full names sorted by last name in either ascending or descending order
    # add doctests make sure it passes

    '''
    >>> sort_by_last_name(['Bob Smith', 'Ken Jones', 'Alex Bradino'], 'ascending')
    ['Alex Bradino', 'Ken Jones', 'Bob Smith']
    '''

    if order == 'ascending':
        return(sorted(people, key=lambda x: x.split(" ")[-1]))
    if order == 'descending':
        return(sorted(people, key=lambda x: x.split(" ")[1]))



# problem 2
# ------------------------------------------------------------------- #
names = ['James', 'Susan', 'Maggie']
ages = [4, 9, 12]


def create_dictionary_from_lists(names, ages):
    # {'James':4, 'Susan':9, 'Maggie':12}
    # add doctests make sure it passes
    '''
    >>> create_dictionary_from_lists(['Mark'], [55])
    {'Mark': 55}
    '''

    # from collections import defaultdict
    # d = defaultdict(int)
    d = {}
    for i in range(len(names)):
        d[names[i]] = ages[i]
    return(d)

    # pass


# problem 3
# ------------------------------------------------------------------- #
numbers = [5, 6, 7, 8, 9, 10, 11, 12]


def square_even_values_and_sum_under_10(numbers):
    # 6^2 + 8^2]
    # add doctests make sure it passes

    '''
    >>> square_even_values_and_sum_under_10([1,2,4,12])
    20
    '''

    a = [x**2 for x in numbers if x < 10 and x%2 ==0]
    return(sum(a))
