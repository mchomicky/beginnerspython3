def is_prime(n, i=2):
    if n == 2:
        return True
    elif not n % i and not n == i:
        return False
    else:
        return is_prime(n, i + 1) if i < n else True


print('is_prime(3):', is_prime(3))
print('is_prime(7):', is_prime(7))
print('is_prime(9):', is_prime(9))
print('is_prime(31):', is_prime(31))
