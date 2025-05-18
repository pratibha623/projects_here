import random

print("***********Welcome to the Number Guessing Game!*************")
print("I am thinking of a number between 1 and 100.")
level = input("Choose difficulty level (easy/hard): ").lower()
chosen_number = random.randint(1, 100)

attempts = 10 if level == "easy" else 5

while attempts > 0:
    print(f"You have {attempts} attempts remaining.")
    guess = int(input("Make a guess: "))

    if guess == chosen_number:
        print(f"🎉 Correct! The number was {chosen_number}. You win!")
        break
    elif guess > chosen_number:
        print("📈 Too high.")
    else:
        print("📉 Too low.")

    attempts -= 1  # Only once here

if attempts == 0:
    print("😞 You Lose.")
    print("The correct number was:", chosen_number)
