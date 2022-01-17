print("Welcome to my quiz")
check = str(input("Press yes to play quiz:"))

if (check.upper() == "YES"):
    print("Okay, let's begin")
    my_dict = {
        "ques1" : "What is the full form of CPU?\n A) Central processing unit\n B) Cat parrot unit\n",
        "ques2" : "What is shortcut key to close button?\n A) Control + F4\n B) control + shift\n",
        "ques3" : "What is the best programming language?\n A) c++ \n B) Python\n"
        }
    check_ques = input(my_dict["ques1"]  )
    checkques = check_ques.upper() 
    if (checkques == "A"):
        print("correct")
    else:
        print("Wrong")
    check_ques = input(my_dict["ques2"])
     
    if (checkques == "A"):
        print("correct")
    else:
        print("Wrong")
    check_ques = input(my_dict["ques3"])
  
    if (checkques== "B"):
        print("Correct")  
    else:
        print("Wrong")   
    print("Thanks for playing")   
else:
    print("Okay, come back when you want to play \n Thanks for Coming")



