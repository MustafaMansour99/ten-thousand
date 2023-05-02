from ten_thousand.game_logic import GameLogic
# from game_logic import GameLogic

calculater = GameLogic.calculate_score

dice_roller = GameLogic.roll_dice
cheat= GameLogic.validate_keepers
scores = GameLogic.get_scorers

def play (roller = GameLogic.roll_dice):

    """
    this function starts the game when called
    """
    '''
    to get the numbers that inside .txt to use it in the test cases
    '''
    global dice_roller
    dice_roller = roller

    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")

    input_user = input('> ')
    if input_user == "n":
        end_game()
    if input_user  == 'y':
        print(f'Starting round 1')
        start_round(round = 1 ,total=0, dice = 6 , point=0)

def end_game ():
        """
        this function return a answer once the user wrote n in the beganing of runing this code
        """
        
        return print('OK. Maybe another time') 



def start_round(round = 1 , total = 0 ,point = 0 , dice = 6):
    '''
    this function will start the game once the plyer enterd y 
    '''
    first_roll = dice_roller(dice) # بدي يطبع 6 ارقام بين (1,6 )
    
    random_num = ''
    for i in first_roll:
         random_num += str(i)+" "

   
    print(f'Rolling {dice} dice...')
    print(f'*** {random_num}***')
    """
    zilch test when the random_num didnt give the user score its appere
    """
    if calculater(first_roll) == 0:
              print("****************************************")
              print("**        Zilch!!! Round over         **")
              print("****************************************")
              print(f"You banked 0 points in round {round}")
              print(f"Total score is {total} points")
              round +=1
              print(f'Starting round {round}')
              point = 0
              return start_round(round,total,dice=6)
    print('Enter dice to keep, or (q)uit:')
    user_choices = input ('> ').replace(" ","")

    if user_choices =='q':
        quit_game(total)

    else :
         
         dice_to_keep = tuple(int(x) for x in user_choices) # حولناها ل تابل عشان الكالكوليتر بستقبل تابل جواتو ارقام من نوع انتيجر
         cheat_test =cheat(first_roll,dice_to_keep)
         """
         Cheat >> when the user try to input the wrong number out range the random number (roll dice) 
         """
         while cheat_test ==False:
              print("Cheater!!! Or possibly made a typo...")
              print(f'*** {random_num}***')
              print('Enter dice to keep, or (q)uit:')
              user_choices = input ('> ').replace(" ","")
              if user_choices =='q':
                return quit_game(total)
              else:
                   dice_to_keep = tuple(int(x) for x in user_choices)
                   cheat_test =cheat(first_roll,dice_to_keep)
         hot_dice =scores(dice_to_keep)
              

                 

         new_dice = dice - len(dice_to_keep) # we get the dice that we enterd in the function (6) and subtract it from the length of inputs that the plyer enterd (user_choices)
         point += calculater(dice_to_keep) # point was 0 so we should add the points regarding the input that the users entered (using calculate score function)

         if len(hot_dice) == 6:
              return hot_dice2(round,total,point,new_dice)


         print(f'You have {point} unbanked points and {new_dice} dice remaining')
         print('(r)oll again, (b)ank your points or (q)uit:')
         user_choices = input ('> ')

         if user_choices =='q':
             quit_game(total)

         if user_choices =='b':
              banked_choice(round , total ,point)
         if user_choices == 'r':
             if new_dice > 0 :
                start_round(round , total ,point,new_dice)
             else :
                  round +=1
                  print('you dont have any more dices play again')
                  start_round(round,total,point,dice=6)   
           

def banked_choice(round , total ,point):
     '''
     will banked the total score 
     '''
     print(f'You banked {point} points in round {round}')
     total += point
     print(f'Total score is {total} points')
     round +=1
     print(f'Starting round {round}')

     start_round(round,total)
      

def quit_game(total):
     '''
     this will quit the game if the plyer enterd q 
     '''
     print(f'Thanks for playing. You earned {total} points')
"""
this function hot dice implement in the first game when the rool dice give six digit all this give me score
"""
def hot_dice2(round,total,point,new_dice):
     print(f'You have {point} unbanked points and 6 dice remaining')
     print('(r)oll again, (b)ank your points or (q)uit:')
     user_choices = input ('> ')

     if user_choices =='q':
        quit_game(total)

     if user_choices =='b':
            banked_choice(round , total ,point)
     if user_choices == 'r':
        if new_dice > 0 :
            start_round(round , total ,point,new_dice)
        else :
            start_round(round,total,point,dice=6)





if __name__ == "__main__":
    play()