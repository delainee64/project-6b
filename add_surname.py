# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 10/30/2022
# Description: Write a function that takes as a parameter a list of first names. It should use a
# list comprehension to return a list that contains only those names that start with a "K",
# but with the surname "Kardashian" added to each one.

def add_surname(first_name):
    """Finds all first names that start with a letter "K" and adds them to the surname "Kardashian". """
    all_names = [name + ' Kardashian' for name in first_name if name[0] == 'K']
    return all_names


first_name = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]

# print(add_surname(first_name))
