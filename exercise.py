# problem 1
# ------------------------------------------------------------------- #
people = ['Bob Smith', 'Ken Jones', 'Alex Bradino']


def sort_by_last_name(people, order):
    # return full names sorted by last name in either ascending or descending order
    # add doctests make sure it passes
    """

    """
    if order == 'asc':
        order = True
    else:
        order = False

    last_name_sort = sorted(list(zip([name.split()[1] for name in people], \
                    [name.split()[0] for name in people])), reverse=order)

    x = [' '.join(last_name_sort[x][0:2]) for x in range(len(last_name_sort))]

    return x

'''

# problem 2
# ------------------------------------------------------------------- #
names = ['James', 'Susan', 'Maggie']
ages = [4, 9, 12]


def create_dictionary_from_lists(names, ages):
    # {'James':4, 'Susan':9, 'Maggie':12}
    # add doctests make sure it passes
    pass


# problem 3
# ------------------------------------------------------------------- #
numbers = [5, 6, 7, 8, 9, 10, 11, 12]


def square_even_values_and_sum_under_10(numbers):
    # 6^2 + 8^2]
    # add doctests make sure it passes
    pass
'''
