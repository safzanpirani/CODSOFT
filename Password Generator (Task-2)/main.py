import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on user's choice of complexity
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the length is at least 8 characters
    length = max(length, 8)

    # Generate a password by randomly selecting characters from the combined set
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Prompt the user for the desired password length
try:
    password_length = int(input("Enter the desired password length (minimum 8 characters): "))
    generated_password = generate_password(password_length)
    print("Generated password:", generated_password)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
