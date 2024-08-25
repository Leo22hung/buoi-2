import math

def is_number(s):
    """Kiểm tra xem một chuỗi có phải là số hay không"""
    try:
        float(s)
        return True
    except ValueError:
        return False

def sigmoid(x):
    """Hàm sigmoid"""
    return 1 / (1 + math.exp(-x))

def relu(x):
    """Hàm ReLU"""
    return max(0, x)

def elu(x, alpha=0.01):
    """Hàm ELU"""
    return x if x >= 0 else alpha * (math.exp(x) - 1)

# Nhập dữ liệu từ người dùng
x_str = input("Nhập giá trị x: ")
activation_function = input("Nhập tên hàm kích hoạt (sigmoid, relu, elu): ")

# Kiểm tra dữ liệu nhập
if not is_number(x_str):
    print("x phải là một số")
    exit()

x = float(x_str)

if activation_function not in ["sigmoid", "relu", "elu"]:
    print(f"{activation_function} không được hỗ trợ")
    exit()

# Tính toán và in kết quả
if activation_function == "sigmoid":
    result = sigmoid(x)
elif activation_function == "relu":
    result = relu(x)
else:
    result = elu(x)

print(f"{activation_function}: f({x}) = {result}")