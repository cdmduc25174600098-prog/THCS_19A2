def tim_so_le_lon_nhat(a, b, c):
    """
    Hàm tìm số lẻ lớn nhất trong ba số nguyên a, b, c.
    Nếu không có số lẻ nào, trả về -1.
    """
    # Tạo danh sách các số lẻ
    so_le = [x for x in (a, b, c) if x % 2 != 0]
    
    if so_le:  # Nếu có ít nhất một số lẻ
        return max(so_le)
    else:
        return -1


# Ví dụ sử dụng:
print(tim_so_le_lon_nhat(2, 4, 6))    # -1 (không có số lẻ)
print(tim_so_le_lon_nhat(3, 8, 5))    # 5
print(tim_so_le_lon_nhat(7, 11, 2))   # 11
print(tim_so_le_lon_nhat(10, 15, 20)) # 15