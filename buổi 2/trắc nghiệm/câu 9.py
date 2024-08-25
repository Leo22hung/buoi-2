import math

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

def approx_cos(x, n):
  """Xấp xỉ cos(x) bằng dãy Taylor

  Args:
    x: Giá trị của x
    n: Số lần lặp

  Returns:
    Giá trị xấp xỉ của cos(x)
  """

  result = 0
  for i in range(n+1):
    result += (-1)**i * x**(2*i) / factorial(2*i)
  return result
assert round ( approx_cos ( x =1 , n =10) , 2) ==0.54
print ( round ( approx_cos ( x =3.14 , n =10) , 2) )