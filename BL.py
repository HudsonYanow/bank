def floatInputValidator(msg, reMsg):
    """
    Asks the user for an input by printing out msg, 
    then it checks if the input is a float
    if it is not it prints out reMsg 
    and gives the user the ability to put in a new input 
    and returns the validated user input

    Args:
    msg (str): the message for the user when asking for the input
    reMsg (str): the message for the user when an error occured with their original input
    """
    userInput=input(msg)
    while not type(userInput)==float:
        try:
            userInput=float(userInput)
        except Exception as e:
            print(f"the following error has occured {e}")
            userInput=input(reMsg)
    return userInput

def intInputValidator(msg, reMsg):
    """
    Asks the user for an input by printing out msg, 
    then it checks if the input is a integer
    if it is not it prints out reMsg 
    and gives the user the ability to put in a new input 
    and returns the validated user input

    Args:
    msg (str): the message for the user when asking for the input
    reMsg (str): the message for the user when an error occured with their original input
    """
    userInput=input(msg)
    while not type(userInput)==int:
        try:
            userInput=int(userInput)
        except Exception as e:
            print(f"the following error has occured {e}")
            userInput=input(reMsg)
    return userInput

def listTypeValidator(arr, itemType):
    """
    checks if every item in a list is the correct item type as provided

    Args:
    arr (list): this is the list that we want to check
    itemType (type): this is the item type we want to look for
    """
    for item in arr:
        if not type(item)==itemType:
            return False
    return True