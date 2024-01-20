"""
Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', 
determine if the input string is valid or not.

Note that an input string is valid if:

Open brackets must be closed by the same type of brackets
Open brackets must be closed in the correct order
Now that you understand the problem statement correctly let us jump to understanding 
the solution of the problem in detail below.
examples:
 >>> is_valid("{[()]}") 
True
 >>> is_valid("({[]})") 
True
 >>> is_valid("({]})") 
False
 >>> is_valid("([{]})") 
False
"""
