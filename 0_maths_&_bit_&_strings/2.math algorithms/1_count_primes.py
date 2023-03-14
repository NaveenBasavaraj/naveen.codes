# Find all primes upto given number N


class countPrimes:

  def countPrime(n):
    if n <= 1:
      return 0
    count = 0
    for i in range(2, n + 1):
      for j in range(2, int(i**0.5) + 1):
        if not i % j == 0:
          count += 1
    return count

  def seiveOfErathosthenes(n):
    if n <= 1:
      return 0
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
      if is_prime[i]:
        for j in range(i * i, n + 1, i):
          is_prime[j] = False
    return sum(is_prime)
