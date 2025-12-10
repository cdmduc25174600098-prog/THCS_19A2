def tinh_tong_chu_so(n):
    """
    Hàm đệ quy tính tổng các chữ số của n.
    Ví dụ: 123 -> 1 + 2 + 3 = 6
    """
    if n < 10:  # Trường hợp cơ sở: chỉ còn 1 chữ số
        return n
    else:
        return n % 10 + tinh_tong_chu_so(n // 10)


# Ví dụ sử dụng:
print(tinh_tong_chu_so(123))   # 6
print(tinh_tong_chu_so(4567))  # 22
print(tinh_tong_chu_so(9))     # 9