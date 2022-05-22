oct=input("Enter your octal value: ")
#oct=oct.replace(" ","")


def octal_to_str(octal_str):
    '''
    It takes an octal string and return a string
        :octal_str: octal str like "110 145 154"
    '''
    str_converted = ""
    for octal_char in octal_str.split(" "):
        str_converted += chr(int(octal_char, 8))
    return str_converted


print(octal_to_str(oct))
