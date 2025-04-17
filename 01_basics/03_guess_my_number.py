import random

def main():
    # 0 se 99 ke darmiyan ek random number choose karo
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        guess = int(input("Enter a guess: "))
        
        if guess > secret_number:
            print("Your guess is too high")
        elif guess < secret_number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break

# Call main function
if __name__ == '__main__':
    main()