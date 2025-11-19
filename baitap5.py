n = int(input("Nhập n: "))

# S1 = 1 + 2 + ... + n
S1 = 0
for i in range(1, n + 1):
    S1 += i

# S2 = 1*2*3*...*(n-1)
S2 = 1
for i in range(1, n):
    S2 *= i

# S3 = 1 - 1/2 + 1/3 - 1/4 + ... + ((-1)^(n+1))/n
S3 = 0
for i in range(1, n + 1):
    S3 += ((-1)**(i + 1)) / i

# S4 = SUM(k=0 -> n) [ k / (k+2) ]
S4 = 0
for k in range(0, n + 1):
    S4 += k / (k + 2)

print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)