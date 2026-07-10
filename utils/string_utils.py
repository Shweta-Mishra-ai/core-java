"""String manipulation and analysis utility functions."""

def ascii_val(ch: str) -> int:
    """Return the ASCII value of the first character of the string."""
    if not ch:
        raise ValueError("Empty string provided.")
    return ord(ch[0])

def count_characters(s: str) -> dict[str, int]:
    """Count vowels, consonants, digits, spaces, and special characters in a string."""
    counts = {
        "vowels": 0,
        "consonants": 0,
        "digits": 0,
        "spaces": 0,
        "special": 0
    }
    if not s:
        return counts
    
    vowels_chars = "aeiouAEIOU"
    for ch in s:
        if ch in vowels_chars:
            counts["vowels"] += 1
        elif ch.isalpha():
            counts["consonants"] += 1
        elif ch.isdigit():
            counts["digits"] += 1
        elif ch == ' ':
            counts["spaces"] += 1
        else:
            counts["special"] += 1
    return counts

def extract_substring(s: str, start: int, end: int) -> str:
    """Safely extract substring from start index to end index (inclusive)."""
    if s is None:
        return ""
    if start < 0 or end >= len(s) or start > end:
        raise ValueError("Invalid index bounds for substring extraction.")
    return s[start:end + 1]

def find_substring_index(s: str, sub: str) -> int:
    """Return the index of substring within the string, or -1 if not found."""
    if s is None or sub is None:
        return -1
    return s.find(sub)

def is_substring(s: str, sub: str) -> bool:
    """Check if sub is a substring of s."""
    if s is None or sub is None:
        return False
    return sub in s

def lower_to_upper_custom(s: str) -> str:
    """Toggle lowercase to uppercase and uppercase to lowercase using ASCII shifts."""
    if s is None:
        return ""
    result = []
    for c in s:
        o = ord(c)
        if 97 <= o <= 122:  # 'a' <= c <= 'z'
            result.append(chr(o - 32))
        elif 65 <= o <= 90:  # 'A' <= c <= 'Z'
            result.append(chr(o + 32))
        else:
            result.append(c)
    return "".join(result)

def to_title_case(s: str) -> str:
    """Convert a sentence to Title Case by capitalizing the first letter of each word."""
    if not s:
        return ""
    words = s.split()
    title_words = [w[0].upper() + w[1:].lower() if len(w) > 0 else "" for w in words]
    return " ".join(title_words)

def is_palindrome_string(s: str) -> bool:
    """Check if a string is a palindrome, ignoring non-alphanumeric chars and case."""
    if s is None:
        return False
    clean = "".join(ch.lower() for ch in s if ch.isalnum())
    return clean == clean[::-1]

def is_palindrome_number(n: int) -> bool:
    """Check if a number is a palindrome number."""
    val = abs(n)
    s = str(val)
    return s == s[::-1]

def toggle_case(s: str) -> str:
    """Toggles casing of a string using a direct ASCII swap."""
    return lower_to_upper_custom(s)

def analyze_name(name: str) -> str:
    """Analyze name to see if it starts, ends, or contains character 'a'."""
    if not name or not name.strip():
        return "Empty name"
    clean = name.strip().lower()
    starts_with_a = clean.startswith("a")
    ends_with_a = clean.endswith("a")

    if starts_with_a and ends_with_a:
        return "Name starts and ends with a"
    elif starts_with_a:
        return "Name starts with a"
    elif ends_with_a:
        return "Name ends with a"
    elif "a" in clean:
        return "Anywhere a"
    else:
        return "No 'a' found in the name"

def check_alphabets(s: str) -> str:
    """Check if a string contains any alphabet letters.
    
    If yes, return the string; otherwise, return 'string not found'.
    """
    if not s:
        return "string not found"
    for ch in s:
        if ch.isalpha():
            return s
    return "string not found"
