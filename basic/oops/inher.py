# Python support all type of inheritance
class Parent1:
    def func1(self):
        print("I am from parent 1")


class Parent2:
    def func2(self):
        print("I am from parent 2")


# Multiple Inheritance
class Child1(Parent1, Parent2):
    def func3(self):
        print("I am from child 1")


# single and multi level inheritance
class Child2(Child1):
    def func4(self):
        print("I am from child 1")


# creating object
ob1 = Child1()
ob1.func1()
ob1.func2()
ob1.func3()

ob2 = Child2()
ob2.func1()
ob2.func2()
ob2.func3()
ob2.func4()
