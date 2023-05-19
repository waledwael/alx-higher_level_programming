#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_letr = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    letrs = [roman_letr[j] for j in roman_string]
    output = 0
    for i in range(len(letrs)):
        output += letrs[i]
        if letrs[i - 1] < letrs[i] and i != 0:
            output -= (letrs[i - 1] + letrs[i - 1])
    return output
