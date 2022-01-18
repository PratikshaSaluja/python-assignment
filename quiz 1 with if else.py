score=0
print("Welcome to my quiz")
check = input("Press yes to start the quiz:")
chec = check.upper()
if (chec == "YES") :
    print("Let's begin")
    ques = input("what does CPU  stands for?\n A)central processing unit \n B) Contact per unit \n")
   
 
    if (ques.upper() ==  "A"):
        score = score + 1
        print("Correct answer!" ,  " you have gained one more score")
    else:
        print("Sorry! wrong answer")
        print("score :" , score)
        
    ques = input("what does SP  stands for?\n A)Soft Prodigy:\n B) Soft Paradise \n")
    
    if ques.upper() == "A":
        score = score + 1
        print("Correct answer!" ,  " you have gained one more score")
        print("score :" , score)
    else:
        print("Sorry! wrong answer")
        print("score :" , score)
    ques = input("which city is known as pink city?\n A) Nepal\n B) Jaipur \n")
   
    if ques.upper() == "B":
        score = score + 1
        print("Correct answer!" ,  " you have gained one more score")
        print("score :" , score)
    else:
        print("Sorry! wrong answer")
        print("score :" , score)
    ques = input("The worl's largest desert is \n A) Antarctic Desert\n B) Thar Desert \n")
   
    if ques.upper() == "B":
        score = score + 1
        print("Correct answer!" ,  " you have gained one more score")
        print("score :" , score)
    else:
        print("Sorry! wrong answer")
        print("score :" , score)
    ques = input("Where is the gateway of india is located?\n A)New Delhi \n B) Chandigarh \n")
    
    if ques.upper() == "A":
        score = score + 1
        print("Correct answer!" ,  " you have gained one more score")
        print("score :" , score)
    else:
        print("Sorry! wrong answer")
        print("score :" , score)
    print(" Thanks for Playing!")
        
        
else:
    print(" okay, comeback when you feel to play quiz")
    print(" Thanks for Coming!")
