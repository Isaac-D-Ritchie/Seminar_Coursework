"""
Isaac D Ritchie
(1st Year @ Edge hill University) 

Reuseable Functions:
These functions are for input sanitation and validation

"""

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
        print("Input Error")
        return ""




if __name__ == "__main__":
    print("Start Program")