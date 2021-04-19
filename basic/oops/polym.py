# Polymorphism means multiple forms

# declaring class
class Base:
    # declaring method
    def hello(self):
        print(" I am from base class")


# inheritance base class
class Child(Base):
    # method overriding
    def hello(self):
        print(" I am from Child  class")


ob = Child()
ob.hello()

# -------------------------------------- Ending Polymorphism-------------------------------
