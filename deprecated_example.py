# python 3.13
from warnings import deprecated

@deprecated("Please use the new function")
def old_function():
    print("This function is deprecated")

def new_function():
    print("This function is new")

old_function()
