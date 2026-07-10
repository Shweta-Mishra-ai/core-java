"""Array/list processing utility functions."""

from utils.math_utils import is_prime

def array_sum_avg(arr: list[int]) -> tuple[int, float]:
    """Calculate the sum and average of elements in a list.
    
    Returns a tuple: (sum, average).
    """
    if not arr:
        return 0, 0.0
    total = sum(arr)
    return total, total / len(arr)

def get_even_odd_elements(arr: list[int]) -> dict[str, list[int]]:
    """Separate and return even and odd elements from a list."""
    even_list = [val for val in arr if val % 2 == 0]
    odd_list = [val for val in arr if val % 2 != 0]
    return {
        "even": even_list,
        "odd": odd_list
    }

def array_length_primes_check(arr: list[int]) -> list[int]:
    """Find and return all prime numbers inside the list."""
    if not arr:
        return []
    return [val for val in arr if is_prime(val)]

def find_min_max(arr: list[int]) -> dict[str, int]:
    """Find the largest and smallest values along with their indices.
    
    Returns a dict with: 'max_val', 'max_pos', 'min_val', 'min_pos'.
    """
    if not arr:
        return {
            "max_val": 0, "max_pos": -1,
            "min_val": 0, "min_pos": -1
        }
    max_val = arr[0]
    min_val = arr[0]
    max_pos = 0
    min_pos = 0
    for i, val in enumerate(arr):
        if val > max_val:
            max_val = val
            max_pos = i
        if val < min_val:
            min_val = val
            min_pos = i
    return {
        "max_val": max_val,
        "max_pos": max_pos,
        "min_val": min_val,
        "min_pos": min_pos
    }

def is_palindrome_array(arr: list[int]) -> bool:
    """Check if the list elements are a palindrome (symmetric)."""
    if not arr:
        return True
    return arr == arr[::-1]
