a, b, n = input("입력:").split(" ")
a, b = int(a), int(b)
if n == "+":
    print(a + b)
elif n == "-":
    print(a - b)
elif n == "*":
    print(a * b)
else:
    print(a / b)
