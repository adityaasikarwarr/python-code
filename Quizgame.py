questions = (("what is the capital of India"),
             ("what is the currency of India"),
             ("what is the language of India"),
             ("what is the largest city of India"),
             ("what is the smallest state of India"))

options = (("A : New Delhi ", "B : Mumbai", "C : Kolkata", "D : Chennai") ,
           ("A : Rupee ", "B : Dollar", "C : Euro", "D : Yen") ,
           ("A : Hindi ", "B : English", "C : Tamil", "D : Telugu") ,
           ("A : New Delhi ", "B : Mumbai", "C : Kolkata", "D : Chennai") ,
           ("A : Goa ", "B : Kerala", "C : Tamil Nadu", "D : Karnataka") )

answers = ("A", "A", "A", "B", "A")
guesses = []
score = 0
question_num = 0


for question in questions:
    print("----------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    print()
    
    guess = input("enter your guess answer: ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
        print("CORRECT!")
        score += 1
    else :
        print("WRONG!")
        print(f"{answers[question_num]}")
    question_num += 1
    
print("***************************")
print("RESULTS")
print("***************************")
print('answers : ' , end="")
for answer in answers:
    print(answer , end=" ")
print()

print('your guess : ' , end="")
for guess in guesses:
    print(guess , end=" ")
print()

score = int((score / len(questions)) * 100)
print(f"your score : {str(score)} %")

    

