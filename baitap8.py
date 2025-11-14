# Bài 8
X = float(input("nhập cân nặng của bạn : "))
Y = float(input("nhập chiều cao của bạn theo cm :"))
YY = Y /100
Z = X / ( YY**2 )
ZZ = round(Z,2)
print(f"chỉ số BMI của bạn là {Z} và sau khi làm tròn là {ZZ}")