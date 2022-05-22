hex_string= input(" enter your hex number: ")
bytes_object= bytes.fromhex(hex_string)
ascii_string=bytes_object.decode("ASCII")
print(ascii_string)
