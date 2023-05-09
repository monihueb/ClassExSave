a = int(input("give me a number"))
b = int(input("give me another number"))

if  a % 2 == 0 and  b % 2 == 0 :
    c = a + b
    print(c)

if a % 2 > 0 and b % 2 > 0 :
    c = a - b
    print(c)

if a % 2 == 0 and b % 2!= 0 or a % 2 != 0 and b % 2== 0 :
    c = a * b
    print(c)
