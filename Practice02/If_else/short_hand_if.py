# if there is only one statement to execute, then we can put it in the same line as "if" statement.
"""
Example:
One-line if statement:

a = 5
b = 2
if a > b: print("a is greater than b")

"""
# Note: We still need the colon : after the condition.
# if you have one statement for "if" and for "else", we can put them on the same line using conditional expression.
"""
Example:
One-line if/else that prints a value:

a = 2
b = 330
print("A") if a > b else print("B")
"""
# This is called a conditional expression (sometimes known as a "ternary operator").

# PRACTICAL EXAMPLES
"""
Finding the maximum of two numbers:

x = 15
y = 20                                           answer: Maximum value: 20
max_value = x if x > y else y                       
print("Maximum value:", max_value)
"""

"""
Setting a default value:

username = ""                                         answer: Welcome, Guest
display_name = username if username else "Guest"
print("Welcome,", display_name)
"""


#WHEN TO USE SHORTHAND IF:
# The condition and actions are simple
# It improves the codes readability
# You want to make a quick assignment based on a condition