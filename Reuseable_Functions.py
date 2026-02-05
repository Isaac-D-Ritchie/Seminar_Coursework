"""
Isaac D Ritchie
(1st Year @ Edge hill University) 

Reuseable Functions:
These functions are for input sanitation and validation

"""
#============================================================================#

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

#============================================================================#

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

#============================================================================#

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
            print(f"\nError: Value must be between {min_value} and {max_value}")
            continue
        if max_value is not None and int_value > max_value:
            print(f"\nError: Value must be between {min_value} and {max_value}")
            continue

        return int_value
        
#============================================================================#




#Execute if file is run directly
if __name__ == "__main__":
    print("Start Program")
    prompt = "Input:"
    print(get_valid_integer(prompt, -99, 99))