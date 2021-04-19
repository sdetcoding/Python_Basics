# creating abstract class
# importing abstract class


from abc import *


# inheritance abstract class
class Base(ABC):
    @abstractmethod
    def salhike(self, per):  # method without declaration
        pass


# inheritance Base class
class Child(Base):
    def salhike(self, per):   # implementing abstract method
        print(per)


ob = Child()
ob.salhike(20)
