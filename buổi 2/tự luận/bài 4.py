import math

def factorial(n):
    """Tính giai thừa của n"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def approx_sin(x, n):
    """Xấp xỉ sin(x) bằng chuỗi Taylor"""
    result = 0
    for i in range(n):
        result += (-1)**i * x**(2*i+1) / factorial(2*i+1)
    return result

def approx_cos(x, n):
    """Xấp xỉ cos(x) bằng chuỗi Taylor"""
    result = 0
    for i in range(n):
        result += (-1)**i * x**(2*i) / factorial(2*i)
    return result

def approx_sinh(x, n):
    """Xấp xỉ sinh(x) bằng chuỗi Taylor"""
    result = 0
    for i in range(n):
        result += x**(2*i+1) / factorial(2*i+1)
    return result

def approx_cosh(x, n):
    """Xấp xỉ cosh(x) bằng chuỗi Taylor"""
    result = 0
    for i in range(n):
        result += x**(2*i) / factorial(2*i)
    return result

# Ví dụ sử dụng
try:
    x = float(input("Nhập giá trị x (radian): "))
    n = int(input("Nhập số lần lặp: "))
    
    print(f"approx_sin({x}, {n}) = {approx_sin(x, n)}")
    print(f"approx_cos({x}, {n}) = {approx_cos(x, n)}")
    print(f"approx_sinh({x}, {n}) = {approx_sinh(x, n)}")
    print(f"approx_cosh({x}, {n}) = {approx_cosh(x, n)}")
except ValueError:
    print("Vui lòng nhập giá trị số hợp lệ.")
