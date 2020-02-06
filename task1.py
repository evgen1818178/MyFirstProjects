def ostatok(arg):
    if (type(arg) == int):
        arg = arg % 2
        if arg:
            return(0)
        else:
            return(1)