from task1 import ostatok

def perebor(n):
    if (type(n) == int):
        a = 0
        while n >= a:
            if ostatok(a):
                print(a*a)
            else:
                print(a)
            if a>0:
                if not(a % 7) and not(a % 4):
                    a = n
            a = a + 1
    else:
        print("введенные данные не являются числом")


perebor(12)

