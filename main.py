from random import randint

random_num = randint(1, 101)
user_num = 0


def guess_number():
    while True:
        try:
            user_num = int(input("Guess the number: "))
            if user_num in range(1, 101):
                print(f"The number you declared is: {user_num}.")
                if user_num == random_num:
                    print("You win!")
                    return user_num
                elif user_num > random_num:
                    print("To big!")
                    continue
                elif user_num < random_num:
                    print("Too small!")
                    continue
            else:
                print("Number should be between 1 and 100")
                continue
            exit()
        except (ValueError, TypeError):
            print("It's not a number!")


guess_number()

