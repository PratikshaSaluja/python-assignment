print("Welcome to my quiz")
check = input("Press yes to start the quiz:")
chec = check.upper()
if (chec == "YES") :
    print("Let's begin")
    ques = input("what does CPU  stands for?\n A)central processing unit \n B) Contact per unit \n")
    checkques = ques.upper()
 
    if (checkques ==  "A"):
        print("Correct answer!")
    else:
        print("Sorry! wrong answer")
        
    ques = input("what does SP  stands for?\n A)Soft Prodigy:\n B) Soft Paradise \n")
    
    if checkques == "A":
        print("Correct answer!")
    else:
        print("Sorry! wrong answer")
    ques = input("which city is known as pink city?\n A) Nepal\n B) Jaipur \n")
   
    if checkques == "B":
        print("Correct answer!")
    else:
        print("Sorry! wrong answer")
    ques = input("The worl's largest desert is \n A) Antarctic Desert\n B) Thar Desert \n")
   
    if checkques == "B":
        print("Correct answer!")
    else:
        print("Sorry! wrong answer")
    ques = input("Where is the gateway of india is located?\n A)New Delhi \n B) Chandigarh \n")
    
    if checkques == "A":
        print("Correct answer!")
    else:
        print("Sorry! wrong answer")
    print(" Thanks for Playing!")
        
        
else:
    print(" okay, comeback when you feel to play quiz")
    print(" Thanks for Coming!")
