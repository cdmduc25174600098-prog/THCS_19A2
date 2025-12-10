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


def in_so_nguyen_to_trong_khoang(a, b):
    """
    Hàm in ra tất cả các số nguyên tố trong khoảng từ a đến b.
    """
    for num in range(a, b + 1):
        if la_so_nguyen_to(num):
            print(num, end=" ")
    print()  # Xuống dòng sau khi in xong


# Ví dụ sử dụng:
print(la_so_nguyen_to(7))   # True
print(la_so_nguyen_to(10))  # False

in_so_nguyen_to_trong_khoang(10, 50)
# Kết quả: 11 13 17 19 23 29 31 37 41 43 47