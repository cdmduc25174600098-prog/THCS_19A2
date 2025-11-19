import math

# Nhập tử số và mẫu số
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

# Kiểm tra mẫu số khác 0
if mau == 0:
    print("Phân số không hợp lệ vì mẫu số bằng 0.")
else:
    # Tìm ƯCLN của tử và mẫu
    ucln = math.gcd(tu, mau)

    # Rút gọn phân số
    tu_gon = tu // ucln
    mau_gon = mau // ucln

    # In kết quả
    print(f"Phân số tối giản là: {tu_gon}/{mau_gon}")