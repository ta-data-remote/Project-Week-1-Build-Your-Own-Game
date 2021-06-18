#Function for adding the character type input and also check if it is the right input.
def req_check_add (req_char, inp_char):
    
    '''
    Checks the y/n input and adds the characters to the requirements list.
    Input arguments: req_char, inp_char
    Arguemnt types: String, String
    Output: none        
    '''
    requirements = []
    while req_char != "y" and req_char != "n":
        req_char = str(input("Please enter (y/n):"))
    
    if req_char == "y":
        requirements.append(inp_char)

    #print(requirements)
    return requirements

