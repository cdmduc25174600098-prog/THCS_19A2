def tim_so_fibonacci(n):
    """
    Hàm đệ quy tìm số Fibonacci thứ n.
    Dãy Fibonacci: F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2) với n >= 2
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return tim_so_fibonacci(n - 1) + tim_so_fibonacci(n - 2)


# Ví dụ sử dụng:
print(tim_so_fibonacci(0))   # 0
print(tim_so_fibonacci(1))   # 1
print(tim_so_fibonacci(5))   # 5 (dãy: 0,1,1,2,3,5)
print(tim_so_fibonacci(10))  # 55