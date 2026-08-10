import time
score = 0

print("=" * 30)
print("         Quiz App")
print("=" * 30)

def ask_question(title, question, option, correct_option):
    print("\n" + "-" * 30)
    print(title)
    print("\n" + "-" *30)
    print(question)
    print(option)
    
    user = input("Enter the correct option is: ").upper()
    while user not in ["A", "B", "C", "D"]:
        print("InvalidSyntax, please enter one of these four: A/B/C/D")
        user = input("Enter the correct option is: ").upper()
        
    print("Locked your option successfully...")
    print("Countdown start...")
    
    for i in range(3, 0, -1):           
           time.sleep(1)
           print(i)
      
    if user == correct_option:
        print(f"You selected the correct option {correct_option}.")
        return 1
            
    else:
        print(f"You have selected the wrong option\nCorrect option is option {correct_option}")
        return 0 
        

quiz = [
            {"title": "Question 1",
            "question": "Which chemical element has the atomic number 79 ?",
            "option": "A.Silver, B.Gold, C.Platinum, D.Copper",
            "correct_option": "B"},
            
            {"title": "Question 2",
            "question": "Which company develop Python ?",
            "option": "A.Microsoft, B.Google, C.Python software foundation, D.Apple",
            "correct_option": "C"},

            {"title": "Question 3",
            "question": "Which game became famous for the 'Battle Royale' mode ?",
              "option": "A.Minecraft, B.Bgmi(Pubg), C.Clash of clans, D.Subway surfers",
            "correct_option": "B"},

            {"title": "Question 4",
            "question": "Which keyword is used to create a function in Python ?",
            "option": "A.function, B.define, C.def, D.func",
            "correct_option": "C"},



            {"title": "Question 5",
            "question": "Which company developed the unreal engine ?",
            "option": "A.Rockstar games, B.Epic games, C.Ubisoft, D.Valve",
            "correct_option": "B"},
]   

for each_question in quiz:
    score +=ask_question(
        each_question["title"],
        each_question["question"],
        each_question["option"],
        each_question["correct_option"]
)

total = len(quiz)
percentage = (score / total) * 100
print(f"Final score: {score} / {total}")
print(f"percentage: {round(percentage, 2)} %")

if score == total:
    print("5/5 Excellent🏆")
elif score == 4:
    print("4/5 Very good🤩")
elif score == 3:
    print("3/5 Good👍")
elif score <=2:
    print("Keep practicing🥲")
print("=" * 50)
print("        Thank you for visiting our app")
print("=" * 50)          