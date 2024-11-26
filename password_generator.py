import random
import string

def generate_password(length):
    """
    Generates a random password that includes uppercase, lowercase, digits, and special characters.

    :param length: The total length of the password (minimum 8)
    :return: A secure password as a string
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    # Define character pools
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # Ensure all requirements are met by including one character from each pool
    required_chars = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special),
    ]

    # Fill the rest of the password length with random choices from all pools
    all_chars = uppercase + lowercase + digits + special
    remaining_length = length - len(required_chars)
    if remaining_length > 0:
        required_chars.extend(random.choices(all_chars, k=remaining_length))

    # Shuffle to avoid predictable patterns
    random.shuffle(required_chars)

    # Return the password as a string
    return ''.join(required_chars)

if __name__ == "__main__":
    try:
        # Input the desired password length
        length = int(input("Enter the desired password length (minimum 8): ").strip())
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
