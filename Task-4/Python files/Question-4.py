num = int(input("Number : "))
act = num
sm = 0

while num != 0:
    tmp = num%10
    sm = sm*10 + tmp
    num = int(num/10)

if act == sm:
    print("True")
else:
    print("False")
