import random
stop=False
while True:
        print("This is a rock paper scisors game made by gul hussain")
        print("NOTE!!! You can also use shorcut FOR Rock type 1 for paper type 2 for scisor type 3")
        game=("rock","paper","scisor")
        chose=random.choice(game)
        
        playcho=input("tell me your choice...")
        if playcho == "1":
            playcho = "rock"
        elif playcho == "2":
            playcho = "paper"
        elif playcho == "3":
            playcho = "scisor"
        print("computer choice",chose,)
        print("your choice",playcho)
        if playcho==chose:
            print("Tie")
        elif chose == "rock" and playcho=="scisor":
            print("rock beat scisors(computer wins!!)")
        elif chose == "scisor" and playcho=="rock":
            print("rock beat scisors(you wins!!)")
        elif chose == "paper" and playcho=="rock":
            print("paper beat rock(computer wins!!)")
        elif chose == "rock" and playcho=="paper":
            print("paper beat rock(you wins!!)")
        elif chose == "paper" and playcho=="scisor":
            print("scisor beat paper (you wins!!)")
        elif chose == "scisor" and playcho=="paper":
            print("scisor beat paper(computer wins!!)")
        else:print("invalid try again")
        while True:
            con=input("Do you wanna play again?(yes/no)").lower()
            if con=="no":
                print("Ok Bye then!!")
                stop=True
                break
            elif con=="yes":
                print("ok lets restart")
                break
            else:
                print("invalid")
                
        if stop:
            break
        
        
