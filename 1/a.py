def __print_a():
  print('a')


cnt = 0
def print_a():
  global cnt
  __print_a()
  cnt += 1
