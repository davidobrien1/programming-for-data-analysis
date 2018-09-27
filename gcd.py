def  gcd(a, b):
    """
    Returns the greatest common divisor of and b.
    """
    if a < b:
        a, b = b,a

    while b > 0:
        a, b = b, a % b

    return a

print(gcd(50, 20))
print(gcd(22,143))
