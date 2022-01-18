score = 0
print("Welcome to my quiz")
check = str(input("Press yes to play quiz:"))
if (check.upper() == "YES"):
    print("Okay, let's begin")
    my_dict = {
        "ques1" : "What is the full form of CPU?\n A) Central processing unit\n B) Cat parrot unit\n",
        "ques2" : "What does SP stands for\n A) Soft paradise\n B) soft prodigy\n",
        "ques3" : "What is the best programming language?\n A) c++ \n B) Python\n"
        }
    check_ques = input(my_dict["ques1"]  )

    if (check_ques.upper() == "A"):
        score = score + 1
        print("correct" , " you have gained one more score")
        print("score :" , score)
    else:
        print("Wrong")
        print("score :" , score)
    check_ques = input(my_dict["ques2"])
    if (check_ques.upper() == "B"):
        score = score + 1
        print("correct" , " you have gained one more score")
        print("score :" , score)
    else:
        print("Wrong")
        print("score :" , score)
    check_ques = input(my_dict["ques3"])
    if (check_ques.upper()== "B"):
        score=score+1
        print("Correct" , " you have gained one more score")
        print("score :" , score)
    else:
        print("Wrong")
        print("score :" , score)
    print("Thanks for playing")
else:
    print("Okay, come back when you want to play \n Thanks for Coming")






