# Find all primes upto given number N


class countPrimes:

  def countPrime(self, n):
    """
    A function to count the number of prime numbers less than a given number n using a brute-force approach.

    Args:
      n (int): A positive integer.

    Returns:
      int: The number of prime numbers less than n.

    Example:
      >>> obj = countPrimes()
      >>> obj.countPrime(10)
      4
    """
    if n <= 1:
      return 0
    count = 0
    for i in range(2, n + 1):
      for j in range(2, int(i**0.5) + 1):
        if not i % j == 0:
          count += 1
    return count

  def seiveOfErathosthenes(self, n):
    """
    A function to count the number of prime numbers less than a given number n using the Sieve of Eratosthenes method.

    Args:
      n (int): A positive integer.

    Returns:
      int: The number of prime numbers less than n.

    Example:
      >>> obj = countPrimes()
      >>> obj.seiveOfErathosthenes(20)
      8
    """
    if n <= 1:
      return 0
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
      if is_prime[i]:
        for j in range(i * i, n + 1, i):
          is_prime[j] = False
    return sum(is_prime)


obj = countPrimes()
print(obj.seiveOfErathosthenes(30))

