#Bài 1
#x la so luong mua san pham
#G la giá của sản phẩm
#y là số tiền còn lại sau khi làm tròn
x = int(input( "số lượng bạn mua là :"))   
G = int(input( "giá sản phẩm này là:"))
công_thức = (x * G + x * 0.1)
Y=round(công_thức, 2)
print("cảm ơn khách hàng đã sử dụng dịch vụ của chúng tôi")
print(f"số tiền khách hàng phải trả là {công_thức} vnd ")
print(f"số tiền sau khi làm tròn là {Y}")