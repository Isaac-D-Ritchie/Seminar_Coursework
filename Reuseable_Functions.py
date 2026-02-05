"""
Isaac D Ritchie
(1st Year @ Edge hill University) 

Reuseable Functions:
These functions are for input sanitation and validation

"""


#Get safe input
def safe_input(prompt) -> str:
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



# Get non-empty string
def get_non_empty_string(prompt) -> str:
    while True:
        raw_input = safe_input(prompt)
        sanitized_input = raw_input.strip()

        if sanitized_input == "":
            print("\nError: Input cannot be empty")
            continue
        else:
            return sanitized_input



if __name__ == "__main__":
    print("Start Program")
    prompt = "Input:"
    print(get_non_empty_string(prompt))