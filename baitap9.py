# bài 9 
A = int(input("nhập số kW điện bạn cần đổi :"))
if A <= 100 :
   X = A * 1678
   print(f"vậy số tiền điện bạn phải trả là :{X} VNĐ")
elif A <= 200 :
   X = 100*1678 +( A-100)*1734
   print(f"vậy số tiền bạn phải trả là :{X} VNĐ")
elif A <= 300 :
   X = 100*1678 + 100*1734 + (A- 100)*2014
   print(f"vậy số tiền điện bạn phải trả là :{X} VNĐ")
else :
   print("trời nhiều quá")