def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_truncatable_prime(n):
    """
    Check if a number is a truncatable prime.

    A truncatable prime is a prime number that remains prime when digits are successively removed
    from either the left or the right end.

    Args:
        n (int): The number to check for truncatable primality.

    Returns:
        bool: True if the number is a truncatable prime, False otherwise.
    """
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
            return False
    return True


truncatable_primes = []
num = (
    11  # Start checking from 11, as single-digit primes are not considered truncatable
)

while len(truncatable_primes) < 11:
    if is_prime(num) and is_truncatable_prime(num):
        truncatable_primes.append(num)
    num += 1

sum_of_truncatable_primes = sum(truncatable_primes)
print(truncatable_primes)
print("The sum of the eleven truncatable primes is:", sum_of_truncatable_primes)
