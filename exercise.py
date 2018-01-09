# problem 1
# ------------------------------------------------------------------- #
people = ['Bob Smith', 'Ken Jones', 'Alex Bradino']


def sort_by_last_name(people, order):
    # return full names sorted by last name in either ascending or descending order
    # add doctests make sure it passes
    pass


# problem 2
# ------------------------------------------------------------------- #
names = ['James', 'Susan', 'Maggie']
ages = [4, 9, 12]

def create_dictionary_from_lists(names, ages):
    # {'James':4, 'Susan':9, 'Maggie':12}
    # add doctests make sure it passes
    names_dict = {}
    for key, val in zip(names, ages):
        names_dict[key] = val
    return names_dict


# problem 3
# ------------------------------------------------------------------- #
numbers = [5, 6, 7, 8, 9, 10, 11, 12]


def square_even_values_and_sum_under_10(numbers):
    """take the even numbers less than 10 in a list and square them..
    argument: List of numbers
    return:   List of squares of the input even numbers less than 10
    square_even_values_and_sum_under_10([5, 6, 7, 8, 9, 10, 11, 12])
    """
    # 6^2 + 8^2]
    total = 0
    for num in numbers:
        if num < 10:
            if num%2 == 0:
                total = total + (num**2)
    return total
        