def giai_phuong_trinh_bac_nhat(a, b):
    """
    Hàm giải phương trình bậc nhất ax + b = 0
    """
    if a == 0:
        if b == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -b / a
        print(f"Nghiệm của phương trình là x = {x}")

# Ví dụ sử dụng:
giai_phuong_trinh_bac_nhat(2, -4)   # x = 2.0
giai_phuong_trinh_bac_nhat(0, 0)    # vô số nghiệm
giai_phuong_trinh_bac_nhat(0, 5)    # vô nghiệm