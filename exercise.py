# problem 1
# ------------------------------------------------------------------- #
people = ['Bob Smith', 'Ken Jones', 'Alex Bradino']
order = "ascending"

def sort_by_last_name(people, order):
    # return full names sorted by last name in either ascending or descending order
    # add doctests make sure it passes
    #a = people.split(' ')
    ordered_list = sorted(people) #This sorts by first name, not last
    return ordered_list
#sort_by_last_name(people, order)

# problem 2
# ------------------------------------------------------------------- #
names = ['James', 'Susan', 'Maggie']
ages = [4, 9, 12]


def create_dictionary_from_lists(names, ages):
    # {'James':4, 'Susan':9, 'Maggie':12}
    # add doctests make sure it passes
    """
    >>> create_dictionary_from_lists(['James', 'Susan', 'Maggie'], [4, 9, 12])
    {'James': 4, 'Susan': 9, 'Maggie': 12}
    """
    dictionary = dict(zip(names, ages))
    return dictionary

#create_dictionary_from_lists(names, ages)


# problem 3
# ------------------------------------------------------------------- #
numbers = [5, 6, 7, 8, 9, 10, 11, 12]


def square_even_values_and_sum_under_10(numbers):
    # 6^2 + 8^2]
    # add doctests make sure it passes
    """
    >>> square_even_values_and_sum_under_10([5, 6, 7, 8, 9, 10, 11, 12])
    [36, 64]
    """
    new_list = list(filter(lambda n: (n < 10), numbers))
    newer_list = list(filter(lambda n: (n % 2 == 0), new_list))
    newest_list = list(map(lambda n: n**2, newer_list))
    return newest_list

#square_even_values_and_sum_under_10(numbers)
