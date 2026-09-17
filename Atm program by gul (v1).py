import random
def atmpro():
    print("{------------ATM-------------}")
    print("|:- Type 1 for Balance check |")
    print("|:- Type 2 for money deposit |")
    print("|:-Type 3 for money withdrawl|")
    print("|:-   Type 4 for exit        |")
    print("|____________________________|")
print("Ayoo this is an ATM program made by GUL HUSSAIN")
name=input("what is your name?..")
money=(1000)
acc=random.randint(1000000,9999999)
while True:
    
    print (name,"your account number is",acc,)   
    while True:
        
        pas=input("Give password for you acount (1234)")
        if pas== "1234":
            print("Welcome ",name,"To Gul atm")
            break
        else:
            print("invalid try again")
    atmpro()
    inp=input("Choose option from the Above..")
    if inp=="3":
        ded=int(input("How much money do you want to withdraw?...."))
        money=(money-ded)
        print("Deducted sucessfully your new balance is",money,)
    elif inp=="2":
        ask=int(input("Type Amount of money you want to transfer...."))
        money=(money+ask)
        print("Transfer successfull your new balance",money)
    elif inp=="1":
        print("Net Amount In Your Account is",money,"$")
    elif inp=="4":
        print("bye then have a great day!!")
        break
        