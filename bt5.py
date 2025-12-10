def kiem_tra_so_doi_xung(n):
    """
    Hàm kiểm tra xem n có phải là số đối xứng hay không.
    Số đối xứng: khi đọc xuôi hay ngược đều giống nhau.
    Ví dụ: 121, 353, 1221
    """
    # Chuyển số thành chuỗi để dễ so sánh
    chuoi = str(n)
    return chuoi == chuoi[::-1]

# Ví dụ sử dụng:
print(kiem_tra_so_doi_xung(121))   # True
print(kiem_tra_so_doi_xung(353))   # True
print(kiem_tra_so_doi_xung(1221))  # True
print(kiem_tra_so_doi_xung(123))   # False