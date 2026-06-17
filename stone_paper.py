import random
a=random.choice(["stone","paper","scissor"])
a=str(a)

try:
    b=int(input("Press 1:stone\nPress 2:paper\npress 3:scissor:"))
    if b==1:
        b="stone"
    elif b==2:
        b="paper"
    elif b ==3:
        b="scissor"      
    else:
        print(f"bhai 1 ,2 or 3 m s ek na ki {b}")
        exit()
    if a==b:
        print("its draw!")
    elif(a=="stone" and b=="paper")or\
        (a=="paper" and b=="scissor")or\
        (a=="scissor" and b=="stone"):
        print("congrulations! aap jeet gaye <3")
    else:
        print("oops!aagli bar try karna ")
except ValueError:
    print("Sapne dekhna achhi baat hai  :)")
 


    