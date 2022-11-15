"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730548982"


class Simpy:
    """A one-dimension, simpler version of NumPy."""
    values: list[float]

    def __init__(self, input_list: list[float]):
        """Constructor."""
        self.values = input_list
    
    def __repr__(self) -> str:
        """Turns to str format."""
        return f"Simpy({self.values})"

    def fill(self, fill_value: float, number_of_repeats: int) -> None:
        """Fills Simpy with number of repeated floats."""
        i: int = len(self.values)
        while i > 0:
            self.values.pop(i - 1)
            i -= 1
        while i < number_of_repeats:
            self.values.append(fill_value)
            i += 1
        
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills Simpy's values with range of floats."""
        assert step != 0.0
        i: float = start
        if stop > 0:
            while i < stop:
                self.values.append(i)
                i += step      
        else:
            while i > stop:
                self.values.append(i)
                i += step

    def sum(self) -> float:
        """Returns sum of all floats in values."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds one Simpy with another Simpy or a float."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item + rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raises each item in a Simpy's values to the power of another Simpy's values' items or a float."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item ** rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks if each item in a Simpy's values is equal to a float or another Simpy's value's items."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    result.append(True)
                else: 
                    result.append(False)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks if each item in a Simpy's values is greater than a float or another Simpy's value's items."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    result.append(True)
                else: 
                    result.append(False)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returns item at index of Simpy's values that is greater than an int or is ."""        
        result: Simpy = Simpy([])
        if isinstance(rhs, int):
            return self.values[rhs]  
        else:
            for i in range(len(self.values)):
                if rhs[i]:
                    result.values.append(self.values[i])
        return result