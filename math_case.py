x=int(input("Enter the value: "))

match x:
    case 0:
        print("X is Zero: ")
    case 1:
        print("X is One: ")
    case 2:
        print("x Is two")
    case 5:
        print("x is Five")
    case _:
        print(x)
        