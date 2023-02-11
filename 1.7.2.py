def finding_gcd(a, b):
    while b != 0:
        result = b
        a, b = b, a % b
    return result