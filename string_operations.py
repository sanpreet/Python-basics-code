"""
Given a string s representing a password, you need to check if the string is valid or not. A valid string has the following properties:

String must have the length greater than or equal to 10.
String must contain at least 1 numeric character.
String must contain at least 1 uppercase character.
String must contain at least 1 lowercase character.
String must contain at least 1 special character from @#$-*.
"""  
import re


def validate(s):
    
    # Regex to check if a string
    # contains uppercase, lowercase
    # special character & numeric value
    
    flag_length = False
    
    # condition 1
    if len(s) >= 10:
        flag_length = True
    
    # condition 2
    flag_numeric =  False
    for i  in s:
        if i.isdigit():
            flag_numeric = True
    
    # condition 3

    flag_upper =  False
    for i  in s:
        if i.upper():
            flag_upper = True
    
    # condition 4

    flag_lower =  False
    for i  in s:
        if i.lower():
            flag_lower = True
    
    char_list = ['@', '#', '$', '-', '*', '.']
    flag_spe_char = False

    for i in s:
        if i in char_list:
            flag_spe_char = True
    
    if  flag_length and  flag_numeric and flag_upper and flag_lower and flag_spe_char == True:
        return 1
    else:
        return 0
