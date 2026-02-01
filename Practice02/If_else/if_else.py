#The Else Keyword
#The else statement is executed when the if condition (and any elif conditions) evaluate to False.

"""
Example:

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

"""
# In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".

"""
              How Else Works
The else statement provides a default action when none of the previous conditions are true. Think of it as a "catch-all" for any scenario not covered by your if and elif statements.

Note: The else statement must come last. You cannot have an elif after an else.
"""