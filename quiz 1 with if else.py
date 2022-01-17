print("Welcome to my quiz")
check = input("Press yes to start the quiz:")
if (check == "yes") :
    print("Let's begin")
    ques1 = input("what does CPU  stands for?\n A)central processing unit \n B) Contact per unit \n")
    if ques1 == "A":
        print("Correct answer!")
    else:
        print("Sorry! wrong answer")
        
    ques2 = input("what does SP  stands for?\n A)Soft Prodigy:\n B) Soft Paradise \n")
    if ques2 == "A":
        print("Correct answer!")
    else:
        print("Sorry! wrong answer")
    ques3 = input("which city is known as pink city?\n A) Nepal\n B) Jaipur \n")
    if ques3 == "B":
        print("Correct answer!")
    else:
        print("Sorry! wrong answer")
    ques4 = input("The worl's largest desert is \n A) Antarctic Desert\n B) Thar Desert \n")
    if ques4 == "B":
        print("Correct answer!")
    else:
        print("Sorry! wrong answer")
    ques5 = input("Where is the gateway of india is located?\n A)New Delhi \n B) Chandigarh \n")
    if ques5 == "A":
        print("Correct answer!")
    else:
        print("Sorry! wrong answer")
    print(" Thanks for Playing!")
        
        
else:
    print(" okay, comeback when you feel to play quiz")
    print(" Thanks for Coming!")
