def two_sum_list(nums, target):
  hashmap = {}
  two_sums = set()
  for index, value in enumerate(nums):
    diff = target - value
    if diff in hashmap:
      two_sums.add((index, hashmap[diff]))
    hashmap[value] = index
  return two_sums

print(two_sum_list(nums=[2, 7, 11, 15, 3, 6, 5, 4], target=9))
{(1, 0), (5, 4), (7, 6)}
# def replace_string(s):
#   new_str = ""
#   n = 1
#   for c in s:
#     if n > 1 and n % 3 == 0:
#       c = '&'
#     new_str += c
#     n += 1
#   return new_str

# print(replace_string('naveen'))

# def replace_string(s):
#   new_str = ""
#   n = 1
#   for c in s:
#     if n > 1 and n % 3 == 0:
#       c = '&'
#     new_str += c
#     n += 1
#   return new_str

# print(replace_string('naveen'))

from datetime import datetime

start_time = datetime.now()
print(f'start_time: {datetime.now()}')

import functools


def debug(func):
  """Print the function signature and return value"""

  @functools.wraps(func)
  def wrapper_debug(*args, **kwargs):
    args_repr = [repr(a) for a in args]  #1
    kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
    signature = ", ".join(args_repr + kwargs_repr)
    print(f"args {args_repr}, kwargs_repr {kwargs_repr}")
    print(f"Calling {func.__name__}({signature})")
    value = func(*args, **kwargs)
    print(f"Calling {func.__name__} returned ({value})")
    return value

  return wrapper_debug


def debug2(func):
  """Print the function signature and return value"""

  @functools.wraps(func)
  def wrapper_debug(*args, **kwargs):
    args_repr = [repr(a) for a in args]  #1
    kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
    signature = ", ".join(args_repr + kwargs_repr)
    now = datetime.now()
    print(f"func start time: {now}")
    print(f"args {args_repr}, kwargs_repr {kwargs_repr}")
    print(f"Calling {func.__name__}({signature})")
    value = func(*args, **kwargs)
    print(f"Calling {func.__name__} returned ({value})")
    print(f"func total time time: {datetime.now() - now}")
    return value

  return wrapper_debug


@debug2
def make_greeting(name, age=None):
  if age is None:
    return f"Howdy {name}!"
  else:
    return f"Whoa {name}! {age} already, you are growing up!"


print(make_greeting("Naveen"))