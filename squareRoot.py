# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and 
# only the integer part of the result is returned.

# Note: You are not allowed to use any built-in exponent function or 
# operator, such as pow(x, 0.5) or x ** 0.5.

def squareRoot(integer):
    beg, end = 0, integer
    while beg <= end:
        mid = (beg + end) // 2
        if mid * mid <= integer and (mid+1) * (mid+1) > integer:
            return mid
        elif mid * mid  < integer:
            beg = mid + 1
        else:
            end = mid - 1
    
    return 0

print(squareRoot(8))
