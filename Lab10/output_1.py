class BasicCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

class AdvancedCalculator(BasicCalculator):
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Ділення на нуль неможливе"

# Використання коду
advanced_calculator = AdvancedCalculator()
print("Addition: ", advanced_calculator.add(5, 3))
print("Subtraction: ", advanced_calculator.subtract(5, 3))
print("Multiplication: ", advanced_calculator.multiply(5, 3))
print("Division: ", advanced_calculator.divide(5, 3))
