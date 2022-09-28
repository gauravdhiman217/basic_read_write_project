# Health Management System
print("***** Welcome to Health Management System ******")



def datetime():
    """This function is to return time and date """
    import datetime
    return datetime.datetime.now()


def write_diet(Name):
    """THis is to wrire diet of a person """
    if Name == 1:
        op = open("gauravdiet.txt", "r+")
        print("Please enter diet you want to register for gaurav\n")
        wr = input(datetime())
        op.write(wr)
        op.close()
        return print("Your response registered")
    if Name == 2:
        op = open("jassidiet.txt", "r+")
        print("Please enter diet you want to register for jassi\n")
        wr = input(datetime())
        op.write(wr)
        op.close()
        return print("Your response registered")
    if Name == 3:
        op = open("harrydiet.txt", "r+")
        print("Please enter diet you want to register for harry\n")
        wr = input(datetime())
        op.write(wr)
        op.close()
        return print("Your response registered")


def read_diet(Name):
    """ This is to read diet """
    if Name == 1:
        op = open("gauravdiet.txt", "r+")
        r = op.read()
        op.close()
        return print(r)
    if Name == 2:
        op = open("jassidiet.txt", "r+")
        r = op.read()
        op.close()
        return print(r)
    if Name == 3:
        op = open("harrydiet.txt", "r+")
        r = op.read()
        op.close()
        return print(r)


def write_ex(Name):
    """This is to write Exercise """
    if Name == 1:
        op = open("gauravex.txt", "r+")
        print("Please write exercise you want to enter for Gaurav\n")
        wr = input(datetime())
        op.write(wr)
        op.close()
        return print("Your response registered")
    if Name == 2:
        op = open("jassiex.txt", "r+")
        print("Please write exercise you want to enter for Jassi\n")
        wr = input(datetime())
        op.write(wr)
        op.close()
        return print("Your response registered")
    if Name == 3:
        op = open("harryex.txt", "r+")
        print("Please write exercise you want to enter for Harry\n")
        wr = input(datetime())
        op.write(wr)
        op.close()
        return print("Your response registered")


def read_ex(Name):
    """This is to read diet of a person """
    if Name == 1:
        op = open("gauravex.txt", "r+")
        r = op.readline()
        op.close()
        return print(r)
    if Name == 2:
        op = open("jassiex.txt", "r+")
        r = op.readline()
        op.close()
        return print(r)
    if Name == 3:
        op = open("harryex.txt", "r+")
        r = op.readline()
        op.close()
        return print(r)

while True:
    Choice =int(input("Press 1 to Lock Diet/exercise and Press 0 to View Diet/ exercise\n"))
    work = int(input("Press 1 to for diet and Press 0 for excersie\n"))
    na = int(input("Press 1 for Gaurav, 2 for Jassi, 3 for Harry\n"))
    """writing portion """
    if Choice == 0:
        if work == 1:
            read_diet(na)
            continue
        elif work ==0:
            read_ex(na)
            continue
        else:
            print("Your response is in valid")
            continue
    elif Choice == 1:
        if work == 1:
            write_diet(na)
            continue
        elif work == 0:
            write_ex(na)
            continue
        else:
            print("Your response is invalid")
            continue
    else:
        print("your response is invalid ")

    # if Choice == True:
    #     w = bool(work)
    #     if w == True:
    #         """writing diet"""
    #         write_diet(na)
    #     elif w == False:
    #         """writing exercise"""
    #         write_ex(na)
    #     else:
    #         print("Your response was not valid")
    #     """Reading portion """
    # elif x == False:
    #     w = bool(work)
    #     if w == True:
    #          read_diet(na)
    #     elif w == False:
    #         read_ex(na)
    #     else:
    #         print("Your response was not valid")
    c = input("Do you want to continue ?, enter y for Yes, n for no\n")
    if c == "n":
        break
    elif c == "y":
        continue
    else:
         print("invalid input")

