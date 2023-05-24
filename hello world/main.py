a = input("a:")
b = input("b:")
c = input("c:")
print()
b = int(b)
c = int(c)
if a + b > c:
    if b + c > a:
        if a + c > b:
            print("true")
        else:
            print("false")
    else:
        print("false")
else:
    print("false")
