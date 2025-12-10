def kiem_tra_so_armstrong(n):
    """
    Hàm kiểm tra xem n có phải là số Armstrong hay không.
    Số Armstrong: tổng các lũy thừa bậc 3 của các chữ số bằng chính nó.
    Ví dụ: 153 = 1^3 + 5^3 + 3^3
    """
    tong = 0
    for chu_so in str(n):
        tong += int(chu_so) ** 3
    return tong == n

# Ví dụ sử dụng:
print(kiem_tra_so_armstrong(153))  # True
print(kiem_tra_so_armstrong(370))  # True
print(kiem_tra_so_armstrong(371))  # True
print(kiem_tra_so_armstrong(407))  # True
print(kiem_tra_so_armstrong(123))  # False