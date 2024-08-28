import random
import string

def generate_password(length, name, complexity):
   
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    
    if complexity == 1:
        all_characters = lowercase_letters
    elif complexity == 2:
        all_characters = lowercase_letters + uppercase_letters
    elif complexity == 3:
        all_characters = lowercase_letters + uppercase_letters + digits
    elif complexity == 4:
        all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    else:
        print("Invalid complexity level.")
        return None

    
    if length < len(name):
        print("Password length must be at least as long as the name.")
        return None

    
    password_chars = list(name)

    
    if length > len(name):
        password_chars += random.choices(all_characters, k=length - len(name))

    
    random.shuffle(password_chars)

    
    return ''.join(password_chars)

def main():
    print("Password Generator")

    try:
        name = input("Enter your name: ")
        length = int(input("Enter the desired length of the password: "))
        complexity = int(input("Enter complexity level (1: lowercase, 2: lowercase+uppercase, 3: lowercase+uppercase+digits, 4: lowercase+uppercase+digits+symbols): "))

        if length < 1:
            print("Password length must be at least 1 character.")
            return

       
        password = generate_password(length, name, complexity)
        if password:
            print(f"Generated password: {password}")

    except ValueError:
        print("Invalid input. Please enter numeric values for the password length and complexity level.")

if __name__ == "__main__":
    main()


