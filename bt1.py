def chuyen_doi_nhiet_do(do_c):
    """
    Hàm chuyển đổi nhiệt độ từ độ C sang độ F.
    Công thức: F = C * 9/5 + 32
    """
    do_f = do_c * 9/5 + 32
    return do_f

# Ví dụ sử dụng:
print(chuyen_doi_nhiet_do(0))    # 32.0
print(chuyen_doi_nhiet_do(100))  # 212.0
print(chuyen_doi_nhiet_do(37))   # 98.6