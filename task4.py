def TypeDetect(arg):
    if (type(arg) == tuple):
        return(1)
    elif (type(arg) == list):
        return(2)
    elif (type(arg) == dict):
        return(3)
    elif (type(arg) == int):
        return(4)
    elif (type(arg) == str):
        return(5)
    elif (type(arg) == float):
        return(6)
    else:
        return('TypeError')


a = (1, 2 ,3)
print(TypeDetect(a))

a = list('abc')
print(TypeDetect(a))

a = {}
print(TypeDetect(a))

a = 1
print(TypeDetect(a))

a = 'a'
print(TypeDetect(a))

a = 1.5
print(TypeDetect(a))

a = open('task3.py', 'r')
print(TypeDetect(a))