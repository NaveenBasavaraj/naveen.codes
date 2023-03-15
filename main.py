class CheckPrime:
  '''
  given a number find if its prime
  '''

  def is_prime(self, num):
    if num < 2 or num % 2 == 0:
      # for negative or if can be divided by 2
      return False
    elif num == 2:
      # 2 is prime
      return True
    else:
      for i in range(3, int(num**0.5) + 1, 2):
        # it is enough to check till sqrt of num
        # step size is kept 2 so that we check only odds
        if num % i == 0:
          return False
        return True

  def is_prime_no_sqrt(self, num):
    if num < 2 or num % 2 == 0:
      # for negative or if can be divided by 2
      return False
    elif num == 2:
      # 2 is prime
      return True
    else:
      for i in range(3, num, 2):
        # step size is kept 2 so that we check only odds
        if num % i == 0:
          return False
        return True


checker = CheckPrime()

num1 = 23
num2 = 10

print(f"{num1} is prime: {checker.is_prime(num1)}")
print(f"{num2} is prime: {checker.is_prime(num2)}")
print(f"{num1} is prime: {checker.is_prime_no_sqrt(num1)}")
print(f"{num2} is prime: {checker.is_prime_no_sqrt(num2)}")
