# from random import randint

# class GuessingGame:
#     def __init__(self, random_num, user_num):
#         self.random_num = random_num
#         self.user_num = user_num
#         random_num = randint(1, 101)
#         user_num = 0
#
#
#     def number_input():
#         while True:
#             try:
#                 self.user_num
#                 user_num = int(input("Guess the number: "))
#                 if user_num in range(1, 101):
#                     exit()
#                 else:
#                     print("Number should be between 1 and 100")
#                     continue
#                 exit()
#             except (ValueError, TypeError):
#                 print("It's not a number!")
#
#
#     def number_check(self, user_num):
#         print(f"The number you declared is: {user_num}.")
#
#
#     number_input()
#     number_check()

from random import randint

random_num = randint(1, 101)
user_num = 0


def number_input():
    while True:
        try:
            user_num = int(input("Guess the number: "))
            if user_num in range(1, 101):
                return user_num
                # exit()
            else:
                print("Number should be between 1 and 100")
                continue
            exit()
        except (ValueError, TypeError):
            print("It's not a number!")


def number_check():
    print(f"The number you declared is: {number_input()}.")


number_check()

