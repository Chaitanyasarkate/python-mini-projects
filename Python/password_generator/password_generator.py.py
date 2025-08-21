import string
from secrets import choice

def generate_password(length=16, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    """Generate a strong random password."""
    chars = ""
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+[]{};:,.<>?/\\|~"

    if not chars:
        raise ValueError("No character sets selected!")

    return "".join(choice(chars) for _ in range(length))

# Example if run directly
if __name__ == "__main__":
    for _ in range(5):
        print(generate_password())
