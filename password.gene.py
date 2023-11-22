import random
import string


def generate_password(length):

    """Generate a random password with the specified length.
    Parameters:
    - length (int): Length of the password.

    Returns:
    - str: Generated password."""

    password_characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

def generate_passwords(num_passwords, length):

    """Generate multiple random passwords.
    Parameters:
    - num_passwords (int): Number of passwords to generate.
    - length (int): Length of each password.

    Returns:
    - list: List of generated passwords."""

    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def main():
    """Main function for the Secure Password Generator."""
    
    print("Welcome to the Secure Password Generator!")
    print("This tool generates strong, secure passwords suitable for various applications.")

    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        length = int(input("Enter the length of each password: "))
    except ValueError:
        print("Please enter valid numeric values.")
        return

    if num_passwords <= 0 or length <= 0:
        print("Number of passwords and length must be greater than 0.")
        return

    passwords = generate_passwords(num_passwords, length)

    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()
