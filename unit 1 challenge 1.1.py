def rec(n):
  if n == 1:
    return n
  else:
    return n * rec(n - 1)


num = int(input("enter a number:"))
if num < 0:
  print("factorial does not exist for negative number")
elif num == 0:
  print("the factorial of 0 is 1")
else:
  print("the factorial of", num, "is", rec(num))
