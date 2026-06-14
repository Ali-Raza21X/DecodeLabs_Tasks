def add():
        
    rent= int(input("enter the flat rent here="))
    food= int(input("enter the food expense here="))
    bills= int(input("enter the total bill amount here="))
    travel=int(input('enter travel expenses'))
    fuel=int(input('enter fuel expenses'))
    funds=int(input('enter funds expenses'))
    total_amount=(rent+food+bills+travel+funds)
    print( "your total amount has to pay",total_amount)

def showmenu():
    while True:
        print("\n-----Expenses Tracker------")
        print("1. Add expenses")
        print("2. Exit System")
        

        choice=input("eneter your choice")

        if choice =="1":
            add()
        elif choice=="2":
            print("Goodbye! you are exiting the system")
            break
        else:
            print('\invalid choice try again')

showmenu()    