import random
secret = int(random.uniform(0,10))
print("I'm thinking of a number between zero and ten."
      , "Can you guess what that is?")
guess = 11


while guess != secret:
    is_number = False
    while not is_number:
        is_number = True
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("I said a number, retard!")
            is_number = False

print("Well done!")
