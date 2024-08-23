class OperatorError(Exception):
    pass

class Calculator:

    def mapper(self, op, num1, num2):
        operator_map = {
            "+" : self.addition,
            "-" : self.subtraction,
            "*" : self.multiplication,
            "/" : self.division,
            "floordiv" : self.floordiv,
            "remainder" : self.remainder,
            "power" : self.power
        }

        try:
            result = operator_map[op](num1, num2)
        except ZeroDivisionError:
            return "Cannot divide by zero"
        except Exception as e:
            return str(e)
        else:
            return result

    def num_formatter(self, n):
        if "." in n:
            return float(n)
        return int(n)
    
    def calculate(self):
        try:
            operator = input("Enter the operator ['+', '-', '*', '/', 'floordiv', 'remainder', 'power']: ")
            if operator not in ['+', '-', '*', '/', 'floordiv', 'remainder', 'power']:
                raise OperatorError("Incorrect operator")
        except OperatorError as e:
            print(e)
            self.calculate()
        else:
            try:
                num1 = self.num_formatter(input("Enter the 1st number: "))
                num2 = self.num_formatter(input("Enter the 2nd number: "))
            except ValueError:
                print("Enter a numeric value!!")
                self.calculate()
            else:
                print(f"Output: {self.mapper(operator, num1, num2)}")
    
    def addition(self, num1, num2):
        return num1 + num2
    
    def subtraction(self, num1, num2):
        return num1 - num2
    
    def multiplication(self, num1, num2):
        return num1 * num2
    
    def division(self, num1, num2):
        return num1 / num2
    
    def remainder(self, num1, num2):
        return num1 % num2
    
    def floordiv(self, num1, num2):
        return num1 // num2
    
    def power(self, num1, num2):
        return num1 ** num2

if __name__ == "__main__":
    c1 = Calculator()
    c1.calculate()
