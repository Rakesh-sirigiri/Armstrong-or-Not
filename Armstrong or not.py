num = int(input("enter 3 digit number :"))
f = num
order = len(str(num))
sum = 0
while(f>0):
    a = f%10
    f = int(f/10)
    sum = sum +(a**order)
if (sum==num):
    print(num,"is an armstrong number")
else:
    print(num,"is not armstrong number")
