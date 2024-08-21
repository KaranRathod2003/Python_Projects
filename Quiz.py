score = 0
questions = [
    ("Is Python a programming language?", True),
    ("Is 5 greater than 10?", False),
    ("Is Earth the third planet from the Sun?", True),
    ("Is 2 + 2 equal to 5?", False),
    ("Is water made of hydrogen and oxygen?", True),
    ("Is the Sun a planet?", False),
    ("Is the capital of France Berlin?", False),
    ("Is Python a type of snake?", True),
    ("Is gravity a force?", True),
    ("Is 1000 meters equal to 1 kilometer?", True)
]

for i in range(10):
    question, correct_ans = questions[i]
    print(question)
    user_answer = input("Enter Your answer True or False: ").capitalize() == 'True'
    if user_answer == correct_ans:
        score+=1
    elif i > 0:
        score -= 1

    if score < 0:
        print(f"Oops! you loose, {score}")
        break
if score == 10:
    print(f"you won reach to the highest score, {score}")
elif score >=0:
    print(f"Your final score is {score}")
