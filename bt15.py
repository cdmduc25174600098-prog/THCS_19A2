def la_so_nguyen_to(n):
    """
    Hàm kiểm tra số nguyên tố.
    Trả về True nếu n là số nguyên tố, ngược lại False.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Nhập vào một số nguyên dương n và kiểm tra
n = int(input("Nhập số nguyên dương n: "))
if la_so_nguyen_to(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")

# In ra các số nguyên tố trong khoảng [100, 500]
print("Các số nguyên tố trong khoảng [100, 500]:")
for num in range(100, 501):
    if la_so_nguyen_to(num):
        print(num, end=" ")