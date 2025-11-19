import math

# Nhập số từ người dùng
n = int(input("Nhập một số nguyên: "))

# Kiểm tra số chính phương
can = math.isqrt(n)  # Lấy căn bậc hai nguyên
if can * can == n:
    print(f"{n} là số chính phương.")
else:
    print(f"{n} không phải là số chính phương.")