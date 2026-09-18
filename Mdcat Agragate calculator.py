print("\033[1mThis is a calculator which takes your metric percentage , Fsc percentage and entry test marks and tells your agregate according to the general mdcat formula(10%+40%+50%)\033[0m")
while True:
    
    while True:
        
        marks=int(input("Put your matric percentage___"))
        if marks<=100:
            break
        elif marks>100:
            print("Invalid max % is 100")
    
    while True:
    
        marks1=int(input("Put your fsc percentage___"))
        if marks1<=100:
            break
        elif marks1>100:
            print("Invalid max % is 100")
    
    while True:
    
        marks2=int(input("Put your mdcat Entrance test score___"))
        if marks2<=180:
            break
        elif marks2> 180:
            print("Invalid max marks is 180")

    mdc=(marks2 / 180) *100
         
    mark=(marks * 0.10)    
        
    mark1=(marks1 * 0.40)
    
    mark2=(mdc *  0.50)
    
    agr=(mark+mark1+mark2)
    
    print("\033[1myour overall mdcat agregate is ",agr,"\033[0m")
    
    again=input("Do you want to calculate again?")
    
    if again in ("no","nahi","na","n"):
        print("Thanks for using bye!!")
        break
    
    elif again in("yes","yeah","han","h","y"):
        print("Ok lets start over")
    