#Bài 2
#X là số kẹo 
#Y là số học sinh
#Z là số kẹo dược chia đều
#C là số kẹo còn thừa
X = int(input("số kẹo ta có là :"))
Y = int(input("số học sinh là :"))
if X < Y :
    print("đen quá không chia được rồi")
else :
 Z = ( X // Y )
 C = ( X % Y)
 print(f"vậy mỗi bạn sẽ được {Z} cái kẹo và còn thừa {C} cái kẹo")