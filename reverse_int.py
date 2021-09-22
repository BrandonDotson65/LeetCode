def reverseInt(integer):
    reversedInt = 0
    if integer < 0:
        symbol = -1
        #ensures proper modulo functionality
        integer = -integer
    else:
        symbol = 1
    
    while integer:
        reversedInt = reversedInt * 10 + integer % 10
        integer = int(integer / 10)

    return symbol * reversedInt if reversedInt <= pow(2, 31) else 0



print(reverseInt(4762))