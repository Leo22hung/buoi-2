import numpy as np

def mae(y_true, y_pred):
    """Tính toán Mean Absolute Error (MAE)"""
    return np.mean(np.abs(y_true - y_pred))

def mse(y_true, y_pred):
    """Tính toán Mean Squared Error (MSE)"""
    return np.mean((y_true - y_pred)**2)

def rmse(y_true, y_pred):
    """Tính toán Root Mean Squared Error (RMSE)"""
    return np.sqrt(np.mean((y_true - y_pred)**2))

def calculate_loss(loss_function, y_true, y_pred):
    """Hàm tính toán loss chung"""
    if loss_function == 'MAE':
        return mae(y_true, y_pred)
    elif loss_function == 'MSE':
        return mse(y_true, y_pred)
    elif loss_function == 'RMSE':
        return rmse(y_true, y_pred)
    else:
        raise ValueError("Hàm loss không hợp lệ")

# Ví dụ sử dụng
try:
    # Nhập số lượng samples
    num_samples = int(input("Nhập số lượng samples: "))
    
    if num_samples <= 0:
        raise ValueError("Số lượng samples phải là một số nguyên dương")
    
    # Nhập tên hàm loss
    loss_name = input("Nhập tên hàm loss (MAE, MSE, RMSE): ").upper()

    if loss_name not in ['MAE', 'MSE', 'RMSE']:
        raise ValueError("Tên hàm loss không hợp lệ. Chỉ chấp nhận MAE, MSE, RMSE.")

    # Tạo dữ liệu ngẫu nhiên
    y_true = np.random.uniform(0, 10, num_samples)
    y_pred = np.random.uniform(0, 10, num_samples)

    # Tính toán loss
    loss = calculate_loss(loss_name, y_true, y_pred)

    # In kết quả
    print(f"Loss ({loss_name}): {loss}")

except ValueError as e:
    print(e)
