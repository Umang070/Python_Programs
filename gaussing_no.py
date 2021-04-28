# import random  TRUE......BREAK;
 win_no=random.randint(1,100)
# 
# win_no=17
guess_count=1
no=int(input("GUESS A NUMBER BETWEEN 1 AND 100 : "))
game_over=False

while not game_over:
            if no == win_no:
                print(f"U WIN AND U GUESSED NUMBER in {guess_count} TRYLE :")
                    game_over = True
            
           else:
                    if no < win_no:
                        print("TOO LOW")
                    else:
                        print("TOO HIGH")
            guess_count += 1
            no=int(input("GUESS AGAIN : "))
                