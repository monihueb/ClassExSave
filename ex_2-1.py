a = int(input("What is your age?"))
print(a)
if a < 18:
    b = 18 - a
    print("you will turn 18 in {} years".format(b))
if a == 18:
    print("You are 18!")
if a > 18:
    b = a - 18
    print("you turned 18 {} years ago".format(b))
