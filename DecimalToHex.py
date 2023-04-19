def decimal_to_hex():
    import struct

    user_num = float(input("Enter a deciaml: "))
    return hex(struct.unpack('<I', struct.pack('<f', user_num))[0])


hex = decimal_to_hex()
print("The hexadecimal representation is: {}".format(hex))
