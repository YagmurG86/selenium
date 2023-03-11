def add(x, y, z):
    """
    This is a function for adding 3 numbers.
    param x: number 1
    param y: number 2
    param z: number 3
    return: sum of all params
    """
    return x+y+z

print(add(2,4,6))

# ==========================================

# Positional Arguments -> Just in order
# Requered Arguments -> default behaviour
def sub_demo1(x, y):
    return x-y
print(sub_demo1(10,6))


# Keyword Arguments
def sub_demo2(x, y):
    return x-y
print(sub_demo2(y=3, x=3))


# Optional Arguemts - Just assign default values
def sub_demo4(x=8, y=5):
    return x-y
print(sub_demo4())
print(sub_demo4(10,6))

# ===========================================

# Scope of Variables: see my own word document

# Scope Rules: Local -> Enclosing -> Global -> Buil-In
# Enclosing means from the Parrent scope 

# ===========================================
