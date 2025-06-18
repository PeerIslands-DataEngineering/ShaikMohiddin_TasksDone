
class UnsupportedOperator(Exception):
    def __init__(self, operator):
        self.operator = operator
        super().__init__(f"Unsupported operator: {self.operator}")

class InputMismatched(Exception):
    def __init__(self):
        super().__init__(self)
        

def calculate(a,b,operator):
    try:
        if (isinstance(a, int) and isinstance(b, int)) or (isinstance(a, float) and isinstance(b, float)) or (isinstance(a, float) and isinstance(b, int)) or (isinstance(a, int) and isinstance(b, float)):
            pass 
        else:
            raise InputMismatched("Inputs must be either both integers or both floats.")
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return a / b
        else:
            raise UnsupportedOperator(operator)
    except UnsupportedOperator as e:
        print(e)
    except InputMismatched as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        

print(calculate(10, 5, '='))
print(calculate(10.5, 5, '+'))