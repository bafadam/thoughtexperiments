#test

print("beginning process")
from ticket import Ticket

grandTotal = 0
showDetail = False


for d in range(20):

    winningTicket = Ticket()
    print(f'draw {d + 1} winning ticket: ', winningTicket.numbers, winningTicket.powerball)
    drawingTotal = 0

    for i in range(500000):

        t = Ticket()

        winnings = t.get_winning_total(winningTicket.numbers, winningTicket.powerball)
        grandTotal += winnings
        drawingTotal += winnings

        if winnings > 0 and showDetail == True:

            print(t.numbers, t.powerball)
            print("$" + str(winnings))

            print(t.get_winning_total(winningTicket.numbers, winningTicket.powerball))
        
    print("drawing total: $", '{:10,.0f}'.format(drawingTotal))

print("grand total: $" + '{:10,.0f}'.format(grandTotal))
    

