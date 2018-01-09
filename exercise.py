"""
Run:
    python -m doctest -v exercise.py
"""

# problem 1
# ------------------------------------------------------------------- #
people = ['Bob Smith', 'Ken Jones', 'Alex Bradino']


def sort_by_last_name(people, order):

    """
    Takes a list fo full names sorts by last name in either assending or descending order

    arguments:  list of names
                Assending('A') or Descending ('D')

    return: sorted list
    Doctests:
        >>> sort_by_last_name(['Bob Smith', 'Ken Jones', 'Alex Bradino'],'A')
        ['Alex Bradino', 'Ken Jones', 'Bob Smith'] 
    """
    # return full names sorted by last name in either ascending or descending order
    # add doctests make sure it passes

    if order == 'A':
        return(sorted(people, key=lambda x: x.split()[1]))
    else:
        return(sorted(people, key=lambda x: x.split()[1], reverse=True))
 #   pass


# problem 2
# ------------------------------------------------------------------- #
names = ['James', 'Susan', 'Maggie']
ages = [4, 9, 12]


def create_dictionary_from_lists(names, ages):
    """
    Takes a list of names and adds ages to it to create a new list

    arguments:  list of names
                list of ages

    return: new dictionary of names and ages
    Doctests:
        >>> create_dictionary_from_lists(['James', 'Susan', 'Maggie'],[4, 9, 12])
        {'James':4, 'Susan':9, 'Maggie':12}
    """    
    # {'James':4, 'Susan':9, 'Maggie':12}
    # add doctests make sure it passes

    return dict(zip(names, ages))



# problem 3
# ------------------------------------------------------------------- #
numbers = [5, 6, 7, 8, 9, 10, 11, 12]
  

def square_even_values_and_sum_under_10(numbers):
    """
    Takes a list of numbers and sums the squares of a list of numbers under 10

    arguments:  list of numbers

    return: sum of squares
    Doctests:
        >>> square_even_values_and_sum_under_10([5, 6, 7, 8, 9, 10, 11, 12])
        100
    """ 
    # 6^2 + 8^2]
    # add doctests make sure it passes
    #    
    return sum((n**2) for n in range(numbers) if n%10 == 2 and n <10)