"""Geometry calculations module including areas and perimeters of shapes."""

import math

def circle_area(r: float) -> float:
    """Calculate the area of a circle. Radius must be non-negative."""
    if r < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * r * r

def circle_circumference(r: float) -> float:
    """Calculate the circumference of a circle. Radius must be non-negative."""
    if r < 0:
        raise ValueError("Radius cannot be negative.")
    return 2.0 * math.pi * r

def rect_area(l: float, b: float) -> float:
    """Calculate the area of a rectangle. Dimensions must be non-negative."""
    if l < 0 or b < 0:
        raise ValueError("Dimensions cannot be negative.")
    return l * b

def rect_perimeter(l: float, b: float) -> float:
    """Calculate the perimeter of a rectangle. Dimensions must be non-negative."""
    if l < 0 or b < 0:
        raise ValueError("Dimensions cannot be negative.")
    return 2.0 * (l + b)

def triangle_area(l: float, b: float) -> float:
    """Calculate the area of a triangle given its base (l) and height (b)."""
    if l < 0 or b < 0:
        raise ValueError("Dimensions cannot be negative.")
    return 0.5 * l * b

def triangle_perimeter(l: float, b: float, h: float) -> float:
    """Calculate the perimeter of a triangle given its side lengths."""
    if l < 0 or b < 0 or h < 0:
        raise ValueError("Dimensions cannot be negative.")
    return l + b + h
