# Python is not fully Object oriented programming language

# declaring class
class Demo1:

    # init method or constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Method to sum of 2 Int
    def sum(self):
        return self.a + self.b


# inheritance parent class
class Demo2(Demo1):
    def __init__(self, a, b):
        print(" welcome to child class")
        Demo1.__init__(self, a, b)  # calling parent class constructor


# creating object
obj = Demo2(8, 8)
print("Sum of 2 number : ", obj.sum())


# ---------------------------------- Ending class ------------------------------------------------
