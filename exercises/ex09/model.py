"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi


__author__ = "730548982"  


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other_point: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other_point.x
        y: float = self.y + other_point.y
        return Point(x, y)

    def distance(self, other_point: Point) -> float:
        """Determines the distance between two Point objects."""
        from math import sqrt
        point_distance: float = sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return point_distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Updates the cell's condition."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "blue"
        else:
            return "black"

    def contract_disease(self) -> None:
        """Changes the cell to an infected cell."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Notifies the model if the cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        return False

    def is_infected(self) -> bool:
        """Notifies the model if the cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        return False

    def contact_with(self, other_cell: Cell) -> None:
        """Infects vulnerable cells that come in contact with infected cells."""
        if self.is_vulnerable() and other_cell.is_infected():
            self.contract_disease()
        elif self.is_infected() and other_cell.is_vulnerable():
            other_cell.contract_disease()

    def immunize(self) -> None:
        """Changes the cell's condition to immune."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Notifies the model if the cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        return False


class Model:
    """The state of the simulation."""
    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, initial_infected: int, initial_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if initial_immune < 0 or initial_immune >= cells:
            raise ValueError("Some number of Cell objects less than the total number of Cell objects must begin immune.")
        if initial_infected <= 0 or initial_infected >= cells:
            raise ValueError("Some number of Cell objects less than the total number of Cell objects must begin infected.")
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)  
            cell: Cell = Cell(start_location, start_direction)
            if initial_infected > 0:
                cell.contract_disease()
                initial_infected -= 1
            if initial_immune > 0 and initial_infected == 0:
                cell.immunize()
                initial_immune -= 1
            self.population.append(cell)
                
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y 
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, each_cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if each_cell.location.x > constants.MAX_X:
            each_cell.location.x = constants.MAX_X
            each_cell.direction.x *= -1.0
        if each_cell.location.x < constants.MIN_X:
            each_cell.location.x = constants.MIN_X
            each_cell.direction.x *= -1.0
        if each_cell.location.y > constants.MAX_Y:
            each_cell.location.y = constants.MAX_Y
            each_cell.direction.y *= -1.0
        if each_cell.location.y < constants.MIN_Y:
            each_cell.location.y = constants.MIN_Y
            each_cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Compare distance between Cell objects."""
        i: int = 0
        while i < len(self.population):
            j: int = i + 1
            while j < len(self.population):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
                j += 1 
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        i: int = 0
        for cell in self.population:
            if cell.is_infected():
                i += 1
        if i > 0:
            return False
        else:
            return True
            
