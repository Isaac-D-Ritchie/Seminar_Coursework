"""
Isaac D Ritchie
(1st Year @ Edge hill University) 

Reuseable Functions:
These functions are for input sanitation and validation

"""
#=====================================================================#

#Get safe input
def safe_input(prompt: str) -> str:
    """
    Function to validate safe input
    Arguments:
      prompt - string for input prompt
    Return:
        Input data or empty string if error occurs
    """
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nInput Error")
        return ""

#=====================================================================#

#Get non-empty string
def get_non_empty_string(prompt: str) -> str:
    """
    Function to get non empty string using while loop
    Utilizes safe_input function for input
    Arguments:
        prompt - string for input prompt
    Return:
        Non-empty string
    """
    while True:
        raw_input: str = safe_input(prompt)
        sanitized_input: str = raw_input.strip()

        if sanitized_input == "":
            print("\nError: Input cannot be empty")
            continue
        else:
            return sanitized_input

#=====================================================================#

#Get valid integer with optional range
def get_valid_integer(prompt: str, min_value: int = None,
                       max_value: int = None) -> int:
    """
    Function to get a valid inter within a range if given
    Utilizes safe_input function for input
    Arguments:
        prompt - string for input prompt
        min_value - minimum integer value
        max_value - maximum integer value
    Returns:
        valid integer
    """
    while True:
        raw_input: str = safe_input(prompt)
        sanitized_input: str = raw_input.strip()

        if not sanitized_input:
            print("\nError: Input cannot be empty")
            continue

        try:
            int_value = int(sanitized_input)
        except ValueError:
            print("\nError: Invalid integer")
            continue

        if min_value is not None and int_value < min_value:
            print(f"\nError: Value must be between"
                  f" {min_value} and {max_value}")
            continue
        if max_value is not None and int_value > max_value:
            print(f"\nError: Value must be between"
                  f" {min_value} and {max_value}")
            continue

        return int_value
        
#=====================================================================#

#Get float with optional range
def get_valid_float(prompt, min_value: float = None,
                     max_value: float = None) -> float:
    """
    Function to get a valid float value within a range if given
    Utilizes safe_input function for input
    Arguments:
        prompt - string for float input prompt
        min_value - minimum float value
        max_value - maximum float value
    Returns:
        valid float
    """
    while True:
        raw_input = safe_input(prompt)
        sanitized_input = raw_input.strip()

        if not sanitized_input:
            print("\nError: Input cannot be empty")
            continue

        try:
            float_value = float(raw_input)
        except ValueError:
            print("\nError: Invalid float value")
            continue

        if min_value is not None and float_value < min_value:
            print(f"\nError: Value must be between"
                  f" {min_value} and {max_value}")
            continue
        if max_value is not None and float_value > max_value:
            print(f"\nError: Value must be between"
                  f" {min_value} and {max_value}")
            continue

        return float_value

#=====================================================================#

def get_choice(prompt, choices: list[str]) -> str:
    lowercase_choices: list[str] = {c.lower(): c for c in choices}
    """
    Function to get choice form a list of strings by converting
    the list keys and input into lowercase to compare
    Arguments:
        prompt - string for choice input prompt
        choices - list of valid choices
    Returns:
        valid list item as a string
    """
    while True:
        raw_input = safe_input(prompt)
        sanitized_key = raw_input.strip().lower()

        if not sanitized_key:
            print("\nError: Input cannot be empty")
            continue

        if sanitized_key not in lowercase_choices:
            options = " - ".join(choices)
            print(f"Error: Please choose from: {options}")
            continue

        return lowercase_choices[sanitized_key]

#=====================================================================#

#Execute code if file is run directly
if __name__ == "__main__":
    print("Start Program")
    username = get_non_empty_string("Enter username: ")
    age = get_valid_integer("Enter age: ", 0, 125)
    role = get_choice("Enter role (Student, Tutor, Admin)",
                       ["Student", "Tutor", "Admin"])
    
    print("\n-- Personal Information --\n"
          f"Username: {username}\n"
          f"Age: {age}\n"
          f"Role: {role}\n"
          )