#!/usr/bin/python3
"""
Write a class MyInt that inherits from int
"""



class MyInt(int):
    def __eq__(self, other):
        """Override the equality operator (==)"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=)"""
        return super().__eq__(other)

    def __str__(self):
        """Override the string representation method"""
        return str(super())

    def __repr__(self):
        """Override the string representation for debugging"""
        return repr(super())
