class ParentClass:
    def __init__(self) -> None:
        print("Parent class instance")

    def parent_method(self):
        print("Parent money")


class ChildClass(ParentClass):
    pass


c = ChildClass()
c.parent_method()

# p = ParentClass()
# p.parent_method()

# ===========================================================

# Multiple Inheritenca: It is possible to inherit from more than one class
# class test (ParentClass, ChildClass)

# Multilevel Inheritance: It is possible that a class is inherint from a class which is inheritng from another class