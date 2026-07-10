"""OOP concepts demonstration module.

Contains multiple inheritance simulations, abstract class behaviors, and simple interest calculations.
"""

from abc import ABC, abstractmethod

# 1. Interface / Multiple Inheritance Simulation
class NewInterface1:
    """Simulates NewInterface1 constant."""
    A = 1000

class NewInterface2:
    """Simulates NewInterface2 constant."""
    A = 2000

class Child(NewInterface1, NewInterface2):
    """Demonstrates multiple inheritance and sum of inherited constants."""
    def expend(self) -> int:
        return NewInterface1.A + NewInterface2.A


# 2. Abstract Class Demonstration
class MyAbs(ABC):
    """Abstract base class demonstrating polymorphism."""
    @abstractmethod
    def calc(self, a: int) -> int:
        pass

    def myprint(self) -> str:
        return "Abstract class print method called"

class Shweta(MyAbs):
    """Subclass implementing square calculation."""
    def calc(self, a: int) -> int:
        return a * a

    def myprint(self) -> str:
        return "Shweta implementation of myprint"

class Ram(MyAbs):
    """Subclass implementing cube calculation."""
    def calc(self, a: int) -> int:
        return a * a * a


# 3. Simple Interest Class
class SimpleInterestCalculator:
    """Simple Interest Calculator class."""
    @staticmethod
    def get_simple_interest(principal: float, rate: float, time: float) -> float:
        """Calculate Simple Interest. Inputs must be non-negative."""
        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("Calculator inputs cannot be negative.")
        return (principal * rate * time) / 100.0
