from calculator import calculation;


class Calculator:
    """Calculator class that maintains history and performs operations."""

    history = []

    @staticmethod
    def add(a: float, b: float) -> float:
        result = a + b
        Calculator.history.append(calculation.Calculation("+", a, b, result))
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        result = a - b
        Calculator.history.append(calculation.Calculation("-", a, b, result))
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        result = a * b
        Calculator.history.append(calculation.Calculation("*", a, b, result))
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        Calculator.history.append(calculation.Calculation("/", a, b, result))
        return result

    @classmethod
    def get_history(cls):
        return [str(calc) for calc in cls.history]