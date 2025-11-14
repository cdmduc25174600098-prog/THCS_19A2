#Bài 6 
# XXXX số năm
XXXX = int(input("nhập số năm :"))
if (XXXX % 400 ==0 )or ((XXXX % 4 ==0) and XXXX % 100 != 0):
   print("Đây là năm nhuận")
else :
   print("năm này ko nhuận rồi ")