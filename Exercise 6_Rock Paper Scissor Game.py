import random
List = ["Rock", "Paper", "Scissor"]
Attempts = 1
User_Score = 0
Engine_Score = 0
while Attempts <= 10:
    Input = input("Rock(R), Paper(P), or Scissor(S) \n")
    Engine = random.choice(List)
    if Input == "R" and Engine == "Rock":
        print(f"Round {Attempts} tied. \n")

    elif Input == "P" and Engine == "Paper":
        print(f"Round {Attempts} tied. \n")

    elif Input == "S" and Engine == "Scissor":
        print(f"Round {Attempts} tied. \n")

    elif Input == "R" and Engine == "Paper":
        Engine_Score += 1
        print(f"You Lose Round {Attempts}. I had {Engine} \n")

    elif Input == "R" and Engine == "Scissor":
        User_Score += 1
        print(f"You Win Round {Attempts}. I had {Engine} \n")

    elif Input == "P" and Engine == "Rock":
        User_Score += 1
        print(f"You Win Round {Attempts}. I had {Engine} \n")

    elif Input == "P" and Engine == "Scissor":
        Engine_Score += 1
        print(f"You Lose Round {Attempts}. I had {Engine} \n")

    elif Input == "S" and Engine == "Rock":
        Engine_Score += 1
        print(f"You Lose Round {Attempts}. I had {Engine} \n")

    elif Input == "S" and Engine == "Paper":
        User_Score += 1
        print(f"You Win Round {Attempts}. I had {Engine} \n")
    print(f"Round {Attempts + 1}")
    print(f"Your Score = {User_Score} \n"
          f"My Score = {Engine_Score} \n")
    Attempts += 1

if User_Score > Engine_Score:
    print("Congratulations on the Win")
elif User_Score < Engine_Score:
    print("Haha, I WON")
else:
    print("We'll settle for a draw")
