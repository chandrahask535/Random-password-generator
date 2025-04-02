# README: Password Generator (TASK 3)

## Author: CHANDRAHAS K

## Batch:(5th NOVEMBER- 5th DECEMBER)

## Domain: PYTHON Programming

## Aim:

To design and build a Python program that generates strong, secure passwords. These passwords should meet modern security standards and be suitable for various applications.

## Libraries Used

The following important libraries were used for this project:
-random
-string

  ## Working of the Code:

 This Python script is a simple Secure Password Generator that allows users to generate random passwords of a specified length. Here's an explanation of how the code works:

1. **Importing Modules:**
   - The script starts by importing the `random` and `string` modules. The `random` module is used to generate random elements, and the `string` module provides a collection of string constants.

2. **`generate_password` Function:**
   - This function takes a parameter `length` and generates a random password of the specified length.
   - It creates a string of possible characters for the password using `string.ascii_letters` (alphabetical characters), `string.digits` (numeric characters), and `string.punctuation` (special characters).
   - The `random.choice` function is then used to randomly select characters from the pool of possible characters, and the loop repeats `length` times to construct the complete password.

3. **`generate_passwords` Function:**
   - This function takes two parameters, `num_passwords` and `length`, and generates a list of random passwords by calling the `generate_password` function `num_passwords` times.

4. **`main` Function:**
   - The `main` function serves as the entry point of the script.
   - It prompts the user to input the number of passwords to generate (`num_passwords`) and the length of each password (`length`).
   - Input validation is performed to ensure that the entered values are numeric.
   - If the input values are valid, the `generate_passwords` function is called, and the generated passwords are displayed to the user.

5. **`__name__ == "__main__"` Check:**
   - The script checks whether it is being run as the main program (not imported as a module). If it is, the `main` function is called.
