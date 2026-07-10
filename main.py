"""Central entry point and interactive command-line interface for Core Java and Python Algorithms.

Provides a CLI menu to execute mathematical, string, geometry, array, OOP, and file operations.
"""

import sys
import unittest
from utils import math_utils, string_utils, geometry_utils, array_utils, oop_demos, file_utils

def clear_screen():
    """Prints spacing to separate menu sections in terminal."""
    print("\n" + "=" * 60 + "\n")

def print_header(title: str):
    """Prints a styled header for sub-menus."""
    print(f"--- {title.upper()} ---")

def get_int_input(prompt: str) -> int:
    """Prompt user for integer input with safety checks."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_float_input(prompt: str) -> float:
    """Prompt user for float input with safety checks."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a valid decimal number.")

def menu_math():
    """Sub-menu for Math and Number Theory algorithms."""
    while True:
        clear_screen()
        print_header("Math & Number Theory Algorithms")
        print("1. Disarium Number Check")
        print("2. Duck Number Check")
        print("3. Happy Number Check")
        print("4. Neon Number Check")
        print("5. Niven (Harshad) Number Check")
        print("6. Prime Number Check")
        print("7. Prime Numbers in Range")
        print("8. Spy Number Check")
        print("9. Magic Number Check")
        print("10. Pronic Number Check")
        print("11. Special (Krishnamurthy) Number Check")
        print("12. Factors of a Number")
        print("13. Factorial calculation")
        print("14. HCF / GCD of Two Numbers")
        print("15. Power Calculation")
        print("16. Square of a Number")
        print("17. Sum of Digits of a Number")
        print("18. Absolute Value")
        print("19. Marks Total & Average (3 Marks)")
        print("20. Back to Main Menu")
        
        choice = get_int_input("\nEnter your choice (1-20): ")
        print()

        if choice == 20:
            break
        elif choice == 1:
            n = get_int_input("Enter integer: ")
            print(f"Result: {n} is {'a Disarium' if math_utils.is_disarium(n) else 'NOT a Disarium'} number.")
        elif choice == 2:
            s = input("Enter number string: ")
            print(f"Result: {s} is {'a Duck' if math_utils.is_duck(s) else 'NOT a Duck'} number.")
        elif choice == 3:
            n = get_int_input("Enter integer: ")
            print(f"Result: {n} is {'a Happy' if math_utils.is_happy(n) else 'NOT a Happy'} number.")
        elif choice == 4:
            n = get_int_input("Enter integer: ")
            print(f"Result: {n} is {'a Neon' if math_utils.is_neon(n) else 'NOT a Neon'} number.")
        elif choice == 5:
            n = get_int_input("Enter integer: ")
            print(f"Result: {n} is {'a Niven' if math_utils.is_niven(n) else 'NOT a Niven'} number.")
        elif choice == 6:
            n = get_int_input("Enter integer: ")
            print(f"Result: {n} is {'a Prime' if math_utils.is_prime(n) else 'NOT a Prime'} number.")
        elif choice == 7:
            start = get_int_input("Enter start range: ")
            end = get_int_input("Enter end range: ")
            print(f"Primes in range: {math_utils.primes_in_range(start, end)}")
        elif choice == 8:
            n = get_int_input("Enter integer: ")
            print(f"Result: {n} is {'a Spy' if math_utils.is_spy(n) else 'NOT a Spy'} number.")
        elif choice == 9:
            n = get_int_input("Enter integer: ")
            print(f"Result: {n} is {'a Magic' if math_utils.is_magic(n) else 'NOT a Magic'} number.")
        elif choice == 10:
            n = get_int_input("Enter integer: ")
            print(f"Result: {n} is {'a Pronic' if math_utils.is_pronic(n) else 'NOT a Pronic'} number.")
        elif choice == 11:
            n = get_int_input("Enter integer: ")
            print(f"Result: {n} is {'a Special' if math_utils.is_special(n) else 'NOT a Special'} number.")
        elif choice == 12:
            n = get_int_input("Enter integer: ")
            print(f"Factors of {n}: {math_utils.get_factors(n)}")
        elif choice == 13:
            n = get_int_input("Enter integer: ")
            try:
                print(f"Factorial of {n} is {math_utils.factorial(n)}")
            except ValueError as ex:
                print(f"Error: {ex}")
        elif choice == 14:
            u = get_int_input("Enter first integer: ")
            v = get_int_input("Enter second integer: ")
            print(f"GCD of {u} and {v} is {math_utils.gcd(u, v)}")
        elif choice == 15:
            base = get_int_input("Enter base: ")
            exp = get_int_input("Enter exponent: ")
            try:
                print(f"{base} ^ {exp} = {math_utils.power(base, exp)}")
            except ValueError as ex:
                print(f"Error: {ex}")
        elif choice == 16:
            n = get_int_input("Enter integer: ")
            print(f"Square of {n} is {math_utils.square(n)}")
        elif choice == 17:
            n = get_int_input("Enter integer: ")
            print(f"Sum of digits of {n} is {math_utils.sum_digits(n)}")
        elif choice == 18:
            n = get_int_input("Enter integer: ")
            print(f"Absolute value of {n} is {math_utils.absolute_val(n)}")
        elif choice == 19:
            print("Enter 3 marks:")
            m1 = get_int_input("Mark 1: ")
            m2 = get_int_input("Mark 2: ")
            m3 = get_int_input("Mark 3: ")
            tot, avg = math_utils.marks_total_avg([m1, m2, m3])
            print(f"Total: {tot} | Average: {avg:.2f}")
        else:
            print("Invalid choice. Try again.")
        
        input("\nPress Enter to continue...")

def menu_string():
    """Sub-menu for String manipulation and analysis."""
    while True:
        clear_screen()
        print_header("String Manipulation & Casing Algorithms")
        print("1. Character ASCII Value")
        print("2. Count Characters (Vowels, Consonants, Digits, etc.)")
        print("3. Extract Substring (Safe bounds)")
        print("4. Substring Search & Existence")
        print("5. Custom Toggle Casing (ASCII Shift)")
        print("6. Word Title Case Conversion")
        print("7. Palindrome String Check")
        print("8. Palindrome Integer Check")
        print("9. Analyze Name (Starts/Ends with 'a')")
        print("10. Check Alphabets Existence")
        print("11. Back to Main Menu")
        
        choice = get_int_input("\nEnter your choice (1-11): ")
        print()

        if choice == 11:
            break
        elif choice == 1:
            s = input("Enter character/string: ")
            try:
                print(f"ASCII value is: {string_utils.ascii_val(s)}")
            except ValueError as ex:
                print(f"Error: {ex}")
        elif choice == 2:
            s = input("Enter sentence: ")
            counts = string_utils.count_characters(s)
            print("Character distribution:")
            for k, v in counts.items():
                print(f"  {k.capitalize()}: {v}")
        elif choice == 3:
            s = input("Enter string: ")
            start = get_int_input("Enter start index: ")
            end = get_int_input("Enter end index: ")
            try:
                sub = string_utils.extract_substring(s, start, end)
                print(f"Extracted Substring: '{sub}'")
            except ValueError as ex:
                print(f"Error: {ex}")
        elif choice == 4:
            s = input("Enter main string: ")
            sub = input("Enter substring to search: ")
            idx = string_utils.find_substring_index(s, sub)
            found = string_utils.is_substring(s, sub)
            print(f"Substring found: {found} (at index {idx})")
        elif choice == 5:
            s = input("Enter string: ")
            print(f"Toggled string: '{string_utils.toggle_case(s)}'")
        elif choice == 6:
            s = input("Enter sentence: ")
            print(f"Title Case: '{string_utils.to_title_case(s)}'")
        elif choice == 7:
            s = input("Enter string: ")
            print(f"Result: '{s}' is {'a palindrome' if string_utils.is_palindrome_string(s) else 'NOT a palindrome'}.")
        elif choice == 8:
            n = get_int_input("Enter integer: ")
            print(f"Result: {n} is {'a palindrome' if string_utils.is_palindrome_number(n) else 'NOT a palindrome'}.")
        elif choice == 9:
            s = input("Enter name string: ")
            print(f"Analysis: {string_utils.analyze_name(s)}")
        elif choice == 10:
            s = input("Enter string: ")
            print(f"Check result: {string_utils.check_alphabets(s)}")
        else:
            print("Invalid choice. Try again.")
            
        input("\nPress Enter to continue...")

def menu_geometry():
    """Sub-menu for Geometry calculations."""
    while True:
        clear_screen()
        print_header("Geometry Area & Perimeter Calculations")
        print("1. Circle Area & Circumference")
        print("2. Rectangle Area & Perimeter")
        print("3. Triangle Area & Perimeter")
        print("4. Back to Main Menu")
        
        choice = get_int_input("\nEnter your choice (1-4): ")
        print()

        if choice == 4:
            break
        elif choice == 1:
            r = get_float_input("Enter radius of circle: ")
            try:
                area = geometry_utils.circle_area(r)
                circ = geometry_utils.circle_circumference(r)
                print(f"Circle (r={r}): Area = {area:.4f} | Circumference = {circ:.4f}")
            except ValueError as ex:
                print(f"Error: {ex}")
        elif choice == 2:
            l = get_float_input("Enter length: ")
            b = get_float_input("Enter breadth: ")
            try:
                area = geometry_utils.rect_area(l, b)
                peri = geometry_utils.rect_perimeter(l, b)
                print(f"Rectangle ({l}x{b}): Area = {area:.4f} | Perimeter = {peri:.4f}")
            except ValueError as ex:
                print(f"Error: {ex}")
        elif choice == 3:
            l = get_float_input("Enter base/side 1: ")
            b = get_float_input("Enter height/side 2: ")
            h = get_float_input("Enter side 3: ")
            try:
                area = geometry_utils.triangle_area(l, b)
                peri = geometry_utils.triangle_perimeter(l, b, h)
                print(f"Triangle: Area (base={l}, height={b}) = {area:.4f} | Perimeter (sides={l},{b},{h}) = {peri:.4f}")
            except ValueError as ex:
                print(f"Error: {ex}")
        else:
            print("Invalid choice.")
            
        input("\nPress Enter to continue...")

def menu_array():
    """Sub-menu for Array and List manipulations."""
    while True:
        clear_screen()
        print_header("Array & List Tools")
        print("1. Compute Sum & Average of a List")
        print("2. Filter Even & Odd Numbers")
        print("3. Extract Primes from List")
        print("4. Find Min/Max Values and Positions")
        print("5. Palindrome Array Check")
        print("6. Back to Main Menu")
        
        choice = get_int_input("\nEnter your choice (1-6): ")
        print()

        if choice == 6:
            break
        
        # Helper to get array from user
        if choice in [1, 2, 3, 4, 5]:
            size = get_int_input("Enter size of list: ")
            if size <= 0:
                print("Size must be positive.")
                input("\nPress Enter to continue...")
                continue
            arr = []
            print(f"Enter {size} integers:")
            for i in range(size):
                arr.append(get_int_input(f"Element {i + 1}: "))
            print(f"\nInput List: {arr}")

            if choice == 1:
                tot, avg = array_utils.array_sum_avg(arr)
                print(f"Sum = {tot} | Average = {avg:.2f}")
            elif choice == 2:
                separated = array_utils.get_even_odd_elements(arr)
                print(f"Even Elements: {separated['even']} (count: {len(separated['even'])})")
                print(f"Odd Elements: {separated['odd']} (count: {len(separated['odd'])})")
            elif choice == 3:
                primes = array_utils.array_length_primes_check(arr)
                print(f"Prime Numbers: {primes}")
            elif choice == 4:
                stats = array_utils.find_min_max(arr)
                print(f"Max Value: {stats['max_val']} at position {stats['max_pos']}")
                print(f"Min Value: {stats['min_val']} at position {stats['min_pos']}")
            elif choice == 5:
                is_p = array_utils.is_palindrome_array(arr)
                print(f"Is Palindrome List? {is_p}")
        else:
            print("Invalid choice.")
            
        input("\nPress Enter to continue...")

def menu_oop():
    """Sub-menu for OOP concept demonstrations."""
    while True:
        clear_screen()
        print_header("Object-Oriented Programming Demos")
        print("1. Multiple Inheritance Constant Sum (Child class)")
        print("2. Polymorphism Abstract Calc (Shweta vs Ram)")
        print("3. Simple Interest Class Calculator")
        print("4. Back to Main Menu")
        
        choice = get_int_input("\nEnter your choice (1-4): ")
        print()

        if choice == 4:
            break
        elif choice == 1:
            c = oop_demos.Child()
            print("Spawning Child class inheriting from NewInterface1 and NewInterface2...")
            print(f"Child.expend() result (Interface Constants sum): {c.expend()}")
        elif choice == 2:
            s = oop_demos.Shweta()
            r = oop_demos.Ram()
            val = get_int_input("Enter value to compute (square and cube): ")
            print(f"Shweta.myprint(): {s.myprint()}")
            print(f"Shweta.calc({val}) [Square]: {s.calc(val)}")
            print(f"Ram.myprint() [Abstract default]: {r.myprint()}")
            print(f"Ram.calc({val}) [Cube]: {r.calc(val)}")
        elif choice == 3:
            p = get_float_input("Enter principal amount: ")
            r = get_float_input("Enter annual rate of interest (%): ")
            t = get_float_input("Enter time period (years): ")
            try:
                si = oop_demos.SimpleInterestCalculator.get_simple_interest(p, r, t)
                print(f"Calculated Simple Interest: {si:.2f}")
            except ValueError as ex:
                print(f"Error: {ex}")
        else:
            print("Invalid choice.")
            
        input("\nPress Enter to continue...")

def menu_file():
    """Sub-menu for File and Folder utility."""
    while True:
        clear_screen()
        print_header("File & Directory Utilities")
        print("1. Safe Directory Creator")
        print("2. Back to Main Menu")
        
        choice = get_int_input("\nEnter your choice (1-2): ")
        print()

        if choice == 2:
            break
        elif choice == 1:
            fname = input("Enter directory name to create: ")
            result = file_utils.create_directory(fname)
            print(result)
        else:
            print("Invalid choice.")
            
        input("\nPress Enter to continue...")

def run_test_suite():
    """Discover and execute the automated unit test suite."""
    clear_screen()
    print_header("Running Automated Unit Test Suite")
    suite = unittest.defaultTestLoader.discover(start_dir='tests', pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    print("\n--- TEST SUMMARY ---")
    print(f"Run: {result.testsRun}")
    print(f"Errors: {len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Success: {result.wasSuccessful()}")

def main():
    """Primary application entry point."""
    while True:
        clear_screen()
        print("*" * 60)
        print("   ☕  WELCOME TO CORE JAVA & PYTHON ALGORITHM LIBRARY  🐍")
        print("*" * 60)
        print("1. Math & Number Theory Algorithms")
        print("2. String Manipulation & Casing Algorithms")
        print("3. Geometry Area & Perimeter Calculator")
        print("4. Array & List processing Tools")
        print("5. Object-Oriented Programming (OOP) Demos")
        print("6. File & Directory System Utilities")
        print("7. Run Automated Diagnostics Test Suite")
        print("8. Exit Application")
        
        choice = get_int_input("\nEnter category (1-8): ")
        
        if choice == 8:
            print("\nExiting. Thank you for using the Algorithm Library!")
            sys.exit(0)
        elif choice == 1:
            menu_math()
        elif choice == 2:
            menu_string()
        elif choice == 3:
            menu_geometry()
        elif choice == 4:
            menu_array()
        elif choice == 5:
            menu_oop()
        elif choice == 6:
            menu_file()
        elif choice == 7:
            run_test_suite()
            input("\nPress Enter to return to main menu...")
        else:
            print("Invalid category choice. Please select 1-8.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
