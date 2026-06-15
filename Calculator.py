import sys
sys.stdout.reconfigure(encoding='utf-8')

num = int(input("数字を入力"))

op = input("演算子を入力")

num2 = int(input("数字を入力"))

if op == "+":
    print(num + num2)
elif op == "-":
    print(num - num2)
elif op == "*":
    print(num * num2)
elif op == "/":
    print(num / num2)
else:
    print(num % num2)