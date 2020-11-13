# Helper function to check if input string is a valid string of vertain legth
def isnotupperstring(inputstring, length):
    if not (type(inputstring) == str and
            len(inputstring) == length and
            inputstring.isalpha() and inputstring.isupper()):
        return True
    else:
        return False
