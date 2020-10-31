
secret_word = "happy"

guess = ""
guess_count = 0
guess_limit = 3

while guess != secret_word and guess_count != guess_limit:
    guess = input("Enter a word: ")
    guess_count += 1
if guess == secret_word:
    print("You Win!")
else: print("You have run out of guesses! You Lose!")
