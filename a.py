import os
import getpass

class OperationsManager():

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        return self.a / self.b
    
    def operation_1(self) -> float:
        """Returns the correct element from the list. If index (self.b) is out of bounds, returns NaN."""
        l = list(range(10)) * self.a
        if self.b > 10:
            return float('nan')
        return l[int(self.b)]


def login_success():
    a = float(input("A = "))
    b = float(input("B = "))
    ops_manager = OperationsManager(a, b)
    print(ops_manager.perform_division())
 
    expression = input('Enter a mathematical formula to calculate: ')
    print ("Result: ", eval(expression))


if __name__ == "__main__":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    if user != "root" or password != "123":
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        login_success()
