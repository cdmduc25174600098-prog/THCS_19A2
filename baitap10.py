# BÀi 10
C = float(input("nhập số lương cơ bản của bạn : "))
B = int(input("nhập số ngày mà bạn đã làm : "))
A = C / 22
if B <= 22 :
    print("bạn đã bị phạt")
    X = A - A * 5/100
    print(f"mức lương của bạn trong tháng này là {X} VNĐ")
else :
    print("bạn được thưởng thêm ")
    X = A + A * 10/100
    print(f"lương của bạn tháng này là {X} VNĐ")