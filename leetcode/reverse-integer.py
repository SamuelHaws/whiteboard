# Runtime: 16 ms, faster than 99.89% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.6 MB, less than 95.09% of Python3 online submissions for Reverse Integer.

def reverse(x: int) -> int:
    x = str(x)
    if len(x) <= 1:
        return x
    # Reverse string
    x = x[::-1]
    # Remove leading 0s
    for c in x:
        if c == '0':
            x = x[1:len(x)]
        if c != '0':
            break
    # Check again for length <= 1 since length may change with leading 0s
    if len(x) <= 1:
        return x
    # Handle negative sign
    if x[len(x)-1] == '-':
        x = x[0:len(x)-1]
        x = '-' + x
    # Check for 32-bit integer overflow
    x = int(x)
    if(abs(x) > (2 ** 31 - 1)):
        return 0
    return x


print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(-120))
print(reverse(0))
print(reverse(100))
print(reverse(1534236469))
