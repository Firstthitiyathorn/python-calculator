class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for _ in range(abs(b)):  
            result = self.add(result, a)
        if b < 0:
            result = -result  
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = 0
        negative_result = (a < 0) != (b < 0)  
        a, b = abs(a), abs(b)
        while a >= b: 
            a = self.subtract(a, b)
            result += 1
        return -result if negative_result else result
    
    def modulo(self, a, b):
        while a >= b:
            a = a-b
        return a



# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))         
    print("Example: subtraction: ", calc.subtract(4, 2))  
    print("Example: multiplication: ", calc.multiply(2, 3))  
    print("Example: division: ", calc.divide(10, 2))      
    print("Example: modulo: ", calc.modulo(10, 3))        
