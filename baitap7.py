# BÀi 7
A = input("vui lòng nhập tên đăng nhập của bạn :")
if A == "admin":
    mật_khẩu = input("nhập mật khẩu vô đây:")
    if mật_khẩu == "passworld_123":
        print("đăng nhập thành công")
    else :
        print(" sai mất rồi thử lai đi nhé")
else :
    print("không tìm thấy tên người dùng vui lòng thử lại sau..")