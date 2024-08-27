import random

print("-" * 20 + " Number Guessing Game " + "-" * 20)
print()

def main():
        playing = True
        while playing:
            low = 1
            high = 100
            target = random.randint(low, high)
            guesses = 0
            
            while True:
                try:
                    guess = input(f"Enter a value between range {low} and {high} : ")
                    guess = int(guess)
                    if low > guess or guess > high:
                        raise Exception
                except Exception:
                    print("Enter a valid number!!")
                else:
                    if guess < target:
                        print("Think Higher!!")
                        guesses += 1
                    elif guess > target:
                        print("think Lower!!")
                        guesses += 1
                    else:
                        print("You Won!!!")
                        print(f"You took {guesses} guesses")
                        break 
            if not input("Do you want to continue playing: ").lower() == 'y':
                playing = False

if __name__ == "__main__":
     main()







