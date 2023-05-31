import os
import getpass
from ast import literal_eval

class OperationsManager():

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        if self.b == 0:
            return float('nan')
        return self.a / self.b
    
    def operation_1(self) -> float:
        """Returns the correct element from the list. If index (self.b) is out of bounds, returns NaN."""
        l = list(range(10)) * self.a
        if self.b >= 10 or self.b <= -11:
            return float('nan')
        return l[self.b]


def login_success():
    a = float(input("A = "))
    b = float(input("B = "))
    ops_manager = OperationsManager(a, b)
    print(ops_manager.perform_division())
 
    expression = input('Enter a mathematical formula to calculate: ')
    print ("Result: ", literal_eval(expression))


if __name__ == "__main__":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    print("Login success!")
    login_success()
