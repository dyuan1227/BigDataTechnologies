def getBinaryRepresentation(x):
    
    if x==0:
        return [0]*64
    # Assigning the sign
    if x > 0:
        sign = [0]
    else:     
        x=abs(x)
        sign = [1]



    # split x into integral and decimal part
    integerpart, decimal = int(x), x - int(x)

    # Change the integerpart to binary
    integer_remainder = []
    while integerpart != 0:
        if integerpart % 2 == 0:
            integer_remainder.append(0)
        else:
            integer_remainder.append(1)
        integerpart = int(integerpart / 2)
    integer_remainder.reverse()

    # Change the fractional part to binary
    fractional_remainder = []
    while decimal != 1.0 and len(fractional_remainder) < 2**11:
        decimal *= 2
        if decimal >= 1.0:
            fractional_remainder.append(1)
            if decimal > 1.0:
                decimal -= 1.0
        else:
            fractional_remainder.append(0)


    # Get the exponent
    if int(x) > 0:
        exponent = len(integer_remainder) - 1 + 1023
    else:
        exponent = -fractional_remainder.index(1) - 1 + 1023

    # Change the exponent to binary
    exp_binary = []
    while exponent != 0:
        if exponent % 2 == 0:
            exp_binary.append(0)
        else:
            exp_binary.append(1)
        exponent = int(exponent / 2)
    exp_binary.reverse()
    exp_binary = [0] * (11 - len(exp_binary)) + exp_binary


    # Creating mantissa by adding integer and fractional
    mantissa = integer_remainder + fractional_remainder
    mantissa = mantissa[mantissa.index(1) + 1:]

    # Modify mantissa to make it length = 52
    if len(mantissa) < 52:
        mantissa += [0] * (52 - len(mantissa))
    if len(mantissa) > 52:
        mantissa = mantissa[:52]

    # concatenate and return the final binary array
    return sign + exp_binary + mantissa

