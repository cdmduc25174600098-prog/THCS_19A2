# BAI 5
# X số tiền muốn gửi
# Y lãi xuất tính theo năm
# Q sau 1 tháng = 1 /12
# W sau 2 quý = 6 tháng = 6/12 = 1/2
# E sau 3 năm
X = int(input("nhập số tiền bạn muốn gửi là :"))
Y = float(input("lãi xuất mà bạn muốn là : "))
YY = Y /100
thang = float(X *YY *1/12)
haiquy = float(X *YY *1/2)
motnam = float(X *YY *3)
print(f"theo dữ liệu mà bạn cung cấp cho chúng tôi với số tiền {X} và lãi xuất {YY} thì :")
print(f"lãi xuất sau 1 tháng là :{thang}")
print(f"lãi xuất sau 2 quý là :{haiquy} ")
print(f"lãi xuất sau 3 năm là :{motnam}")
print("cảm ơn khách hàng đã sử dụng dịch vụ của chúng tôi")