import math

# Nhập hai số nguyên từ người dùng
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

# Tính ƯCLN bằng hàm gcd
ucln = math.gcd(a, b)

# In kết quả
print(f"Ước chung lớn nhất của {a} và {b} là: {ucln}")