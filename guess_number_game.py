'''
AUTHOR : ESUB BEIG
DATE   : 06-07-2019
THEME  : GUISSING NUMBER GAME
'''
from random import randint

class guess_game():

    def __init__(self):
        self.user_num_guess = 0
        self.secrete_num = randint(1,99)
        
    def display_info(self):
        print("""
                !!! WELCOME TO GUESSING NUMBER GAME !!!
                ---------------------------------------
            """)

    def bussiness_logic(self):
        try:
            user_act_guess = int(input('Enter a number b/w (1-99)? '))
            if self.user_num_guess < 4:

                if user_act_guess == self.secrete_num:
                    print('Hurray! Your guessed correct number')
                    #self.status = False
                    self.user_num_guess += 1
                    #break
                elif user_act_guess > self.secrete_num:
                    print('HINT: Try Lesser Number')
                    self.user_num_guess += 1
                    obj.bussiness_logic()

                elif user_act_guess < self.secrete_num:
                    print('HINT: Try Greater Number')
                    self.user_num_guess += 1
                    obj.bussiness_logic()

            elif self.user_num_guess == 4:

                if user_act_guess == self.secrete_num:
                    print('Hurray! Your guessed correct number')
                else:
                    print('SORRY! Out of chances...')

        except Exception as e:
            print(e)

obj = guess_game()
obj.display_info()
obj.bussiness_logic()