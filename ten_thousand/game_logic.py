import random
from collections import Counter

class GameLogic():
    """
    this function roll the dice between number 1-6
    """
    @staticmethod
    def roll_dice(value):
        values = []
        for i in range(value):
            number = random.randint(1,6)
            values.append(number)
        tuples=tuple(values)

        return tuples
    
    """
    this function to calculate score depend the rules of the game
    """
    @staticmethod
    def calculate_score(dice):
        
        score = 0

        dice_set = set(dice)
        pairs = []

        if len(dice) == 0:
            return 0
        
        if dice_set == {1,2,3,4,5,6}:
            score += 1500
            return score

        for i in dice_set: 
            num_of_kinds = dice.count(i)
            if num_of_kinds == 2:
                pairs.append(2)
            if i == 1:
                if num_of_kinds == 1:
                    score += 100
                elif num_of_kinds == 2:
                    score += 200
                elif num_of_kinds == 3:
                    score += 1000
                elif num_of_kinds == 4:
                    score += 2000
                elif num_of_kinds == 5:
                    score += 4000
                elif num_of_kinds == 6:
                    score += 8000
                
            
            elif i == 2:
                if num_of_kinds == 3:
                    score += 200
                elif num_of_kinds == 4:
                    score += 400
                elif num_of_kinds == 5:
                    score += 800
                elif num_of_kinds == 6:
                    score += 1600
                    
            elif i == 3:
                if num_of_kinds == 3:
                    score += 300
                elif num_of_kinds == 4:
                    score += 600
                elif num_of_kinds == 5:
                    score += 1200
                elif num_of_kinds == 6:
                    score += 2400

            elif i == 4:
                if num_of_kinds == 3:
                    score += 400
                elif num_of_kinds == 4:
                    score += 800
                elif num_of_kinds == 5:
                    score += 1600
                elif num_of_kinds == 6:
                    score += 3200
        
            elif i == 5:
                if num_of_kinds == 1:
                    score += 50
                elif num_of_kinds == 2:
                    score += 100   
                elif num_of_kinds == 3:
                    score += 500
                elif num_of_kinds == 4:
                    score += 1000
                elif num_of_kinds == 5:
                    score += 2000
                elif num_of_kinds == 6:
                    score += 4000

            elif i == 6:
                if num_of_kinds == 3:
                    score += 600
                elif num_of_kinds == 4:
                    score += 1200
                elif num_of_kinds == 5:
                    score += 2400
                elif num_of_kinds == 6:
                    score += 4800

            
        if len(pairs) == 3:
            score = 1500
        return score
    """
    to check between 2 tuple depende on test file  
    """
    @staticmethod
    def validate_keepers(roll,keeper):
        roll_counter = Counter(roll)
        keeper_counter = Counter(keeper)
        same = keeper_counter - roll_counter
        if (len(same)==0):
            return True
        else:
             return False
    @staticmethod
    def get_scorers(t):
      calu1 = GameLogic.calculate_score(t)
      arr=[]
      listt =list(t)
      for i,val in enumerate(listt):
          listt.pop(i)
          calu2 = GameLogic.calculate_score(listt)
          if calu1 != calu2:
            arr.append(val)
            listt.insert(i,val)
          else:
              listt.insert(i,val)
                
      tt = tuple(arr)
      return tt 
if __name__ == "__main__":
        print(GameLogic.roll_dice(2))
