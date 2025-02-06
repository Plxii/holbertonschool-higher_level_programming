#!/usr/bin/python3

"""
module 1-my_list contains the class MyList.
"""


class MyList(list):
    """
    MyList is a subclass of the list class.
    It adds a method to print the sorted list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        This method creates a sorted version of the list
        and prints it without modifying the original list.
        @self: The current instance of MyList
        allowing access to its attributes and methods.
        """
        print(sorted(self))
