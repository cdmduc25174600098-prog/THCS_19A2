def la_so_hoan_hao(n):
    """
    Hàm kiểm tra số hoàn hảo.
    Số hoàn hảo: tổng các ước số dương (không kể chính nó) bằng chính nó.
    Ví dụ: 6 = 1 + 2 + 3
    """
    if n < 2:
        return False
    tong_uoc = 1  # luôn có 1 là ước
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            tong_uoc += i
            if i != n // i:  # tránh cộng trùng khi i là căn bậc 2
                tong_uoc += n // i
    return tong_uoc == n


def tinh_tong_so_hoan_hao(a, b):
    """
    Hàm tính tổng các số hoàn hảo trong khoảng [a, b].
    """
    tong = 0
    for num in range(a, b + 1):
        if la_so_hoan_hao(num):
            tong += num
    return tong


# Ví dụ sử dụng:
print(tinh_tong_so_hoan_hao(1, 30))   # 6 + 28 = 34
print(tinh_tong_so_hoan_hao(1, 10000)) # 6 + 28 + 496 + 8128 = 8658