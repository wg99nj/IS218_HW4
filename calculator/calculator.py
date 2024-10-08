class Calculator:
    _history: list[str] = []  # Class-level list to store history of calculations

    @staticmethod
    def add(a: float, b: float) -> float:
        result = a + b
        Calculator._add_to_history(f"add({a}, {b}) = {result}")
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        result = a - b
        Calculator._add_to_history(f"subtract({a}, {b}) = {result}")
        return result

    @classmethod
    def divide(cls, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result = a / b
        cls._add_to_history(f"divide({a}, {b}) = {result}")
        return result

    # Class method to add a custom calculation to the history
    @classmethod
    def _add_to_history(cls, calculation: str) -> None:
        cls._history.append(calculation)

    # Class method to retrieve the last calculation from history
    @classmethod
    def get_last_calculation(cls) -> str:
        if cls._history:
            return cls._history[-1]
        return None

    # Class method to get the entire history
    @classmethod
    def get_history(cls) -> list[str]:
        return cls._history

    # Class method to clear the history (useful for testing)
    @classmethod
    def clear_history(cls) -> None:
        cls._history.clear()