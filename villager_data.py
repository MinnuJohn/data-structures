"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    # TODO: replace this with your code
    file = open(filename)
    for line in file:
        name = line.split("|")
        species.add(name[1])

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    villagers = []
    # TODO: replace this with your code
    file = open(filename)
    for line in file:
        words = line.split("|")
        species = words[1]
        name = words[0]
        if search_string == "All" or search_string == species:
            villagers.append(name)
    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    
    # TODO: replace this with your code
    hobby_name = []
    for i in range(6):
        lst = []
        hobby_name.append(lst)

    cnt = 0
    names = []
    file = open(filename)
    hobby_list=['Fitness','Nature','Education','Music','Fashion','Play']
    for line in file:
        word_list = line.split('|')
        hobby = word_list[3]
        name = word_list[0]
        idx=hobby_list.index(hobby)
        hobby_name[idx].append(name)

    return hobby_name


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code
    file = open(filename)
    for line in file:
        word_list = line.rstrip().split("|")
        all_data.append(tuple(word_list))
    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code
    file = open(filename)
    for line in file:
        words = line.split('|')
        name = words[0]
        motto = words[4]
        if name == villager_name:
            return motto

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code

