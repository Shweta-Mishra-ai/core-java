"""Mathematical algorithms module containing number theory and basic math functions."""

import math

def is_disarium(n: int) -> bool:
    """Check if a number is a Disarium number.
    
    A Disarium number is a number where the sum of its digits powered to their
    respective positions equals the number itself.
    """
    if n < 0:
        return False
    digits = str(n)
    total = sum(int(digit) ** (i + 1) for i, digit in enumerate(digits))
    return total == n

def is_duck(s: str) -> bool:
    """Check if a string representation of a number is a Duck number.
    
    A Duck number is a number which has zero in it, but not at the start.
    """
    if not s:
        return False
    s = s.strip()
    if s.startswith(("-", "+")):
        s = s[1:]
    if not s:
        return False
    return s[0] != '0' and '0' in s

def is_happy(n: int) -> bool:
    """Check if a number is a Happy number.
    
    A Happy number is defined by a process where replacing the number by the
    sum of the squares of its digits eventually leads to 1.
    """
    if n <= 0:
        return False
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

def is_neon(n: int) -> bool:
    """Check if a number is a Neon number.
    
    A Neon number is a number where the sum of digits of its square is equal
    to the number itself.
    """
    if n < 0:
        return False
    square_val = n * n
    return sum(int(digit) for digit in str(square_val)) == n

def is_niven(n: int) -> bool:
    """Check if a number is a Niven (Harshad) number.
    
    A Niven number is an integer that is divisible by the sum of its digits.
    """
    if n <= 0:
        return False
    sum_digits_val = sum(int(digit) for digit in str(n))
    if sum_digits_val == 0:
        return False
    return n % sum_digits_val == 0

def is_prime(n: int) -> bool:
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start: int, end: int) -> list[int]:
    """Return list of prime numbers in range [start, end]."""
    return [i for i in range(start, end + 1) if is_prime(i)]

def is_spy(n: int) -> bool:
    """Check if a number is a Spy number.
    
    A Spy number is a number where the sum of its digits equals the product of its digits.
    """
    val = abs(n)
    if val == 0:
        return False
    digits = [int(d) for d in str(val)]
    sum_digits_val = sum(digits)
    prod_digits_val = math.prod(digits)
    return sum_digits_val == prod_digits_val

def is_magic(n: int) -> bool:
    """Check if a number is a Magic number.
    
    A Magic number is a number in which the eventual sum of digits (recursively)
    equals 1.
    """
    val = abs(n)
    while val > 9:
        val = sum(int(digit) for digit in str(val))
    return val == 1

def is_pronic(n: int) -> bool:
    """Check if a number is a Pronic (oblong) number.
    
    A Pronic number is the product of two consecutive integers: n * (n + 1) = number.
    """
    if n < 0:
        return False
    limit = int(math.isqrt(n))
    for i in range(limit + 1):
        if i * (i + 1) == n:
            return True
    return False

def is_special(n: int) -> bool:
    """Check if a number is a Special number (Krishnamurthy number).
    
    A Special number is a number where the sum of factorials of its digits
    equals the number itself.
    """
    if n <= 0:
        return False
    return sum(math.factorial(int(digit)) for digit in str(n)) == n

def get_factors(n: int) -> list[int]:
    """Return all positive factors of a number."""
    val = abs(n)
    if val == 0:
        return []
    return [i for i in range(1, val + 1) if val % i == 0]

def factorial(n: int) -> int:
    """Calculate the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)

def gcd(u: int, v: int) -> int:
    """Calculate the Greatest Common Divisor / HCF of two integers."""
    return math.gcd(u, v)

def power(base: int, exp: int) -> int:
    """Calculate the power of base raised to exp (exponents >= 0)."""
    if exp < 0:
        raise ValueError("Only non-negative exponents are supported for integer result.")
    return base ** exp

def square(n: int) -> int:
    """Return the square of a number."""
    return n * n

def sum_digits(n: int) -> int:
    """Return the sum of digits of a number."""
    return sum(int(digit) for digit in str(abs(n)))

def absolute_val(n: int) -> int:
    """Return the absolute value of a number."""
    return abs(n)

def marks_total_avg(marks: list[int]) -> tuple[int, float]:
    """Calculate total and average of a list of marks."""
    if not marks:
        return 0, 0.0
    total = sum(marks)
    return total, total / len(marks)
