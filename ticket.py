import random

class Ticket:
    def __init__(self):

        self.numbers = Ticket.generate_numbers()
        self.powerball = random.randint(1,29)   
        
    def generate_numbers():
        numbers = []
        for i in range(5):
            number = random.randint(1,69)
            while number in numbers:
                number = random.randint(1,69)
            
            numbers.append(number)
        return numbers

    def get_winning_total(self, drawNumbers, powerball):

        total = 0

        matchingNumbers = len(set(self.numbers) & set(drawNumbers))
        matchingPowerball = self.powerball == powerball

        if matchingPowerball == True:
            if matchingNumbers == 5:
                total = 10000000
            elif matchingNumbers == 4:
                total = 50000
            elif matchingNumbers == 3:
                total = 100
            elif matchingNumbers == 2:
                total =7
            elif matchingNumbers == 1:
                total = 4
        else:    
            if matchingNumbers == 5:
                total = 1000000
            elif matchingNumbers == 4:
                total = 100
            elif matchingNumbers == 3:
                total = 7
            else:
                total = 0

        return total
            