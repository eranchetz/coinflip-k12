import random
import timeit
import sys

## This program bets on a coinflip against itslef so we can test several betting stratagies
## To run this you should use python3 coinflip.py <number of rounds>
## For example: python3 coinflip.py 100


# get argument form command 
arg1 = int(sys.argv[1])

# timeit will measure how long this code runs
start = timeit.default_timer()

print("🪙 Start Flip a Coin")

# flipcoin() retuns "H" or "T" randonmly 
def flipcoin():
  rand = random.random()
  #print("Random number =", rand)
  if rand > 0.5:
    result = "H"
  else:
    result = "T"
  #print(result)
  return result

# bet(bank,sum) run 2 coinflips() and compares them, if equla the bet is successful
# bank = initla money , num == number of bets
def bet(bank,num):
    initial_bet = 1 #this will be multiplied if we lose
    bet = initial_bet

    # streak and longest streak calculation vars
    streak = 0
    max_streak = 0
    max_count = 0
    prev_loss = False

    print("🤑 You have", bank, "In the bank. Initial bet is ",bet)
    for x in range(num):
        if bank <= 0:
            print("😢 You lost all your money :( 💸")
            break
        elif bank < bet:
            # if we still have money let's bet on all of it
            print("🙀 You almost have no money, we are going all in!")
            bet = bank
        ## Bets start here! 
        if flipcoin() == flipcoin(): #Win Case
            bank = bank + bet
            print("🟢 WIN! \o/ new balance", bank)
            bet = initial_bet 
            if max_streak < streak:
                max_streak = streak
            elif max_streak == streak:
                max_count += 1
            streak = 0 
        else: #Lose case
          bank = bank - bet 
          bet = bet * 2
          streak += 1  
          print("🔴 LOSE! :-( new balance // next-bet :", bank,"//",bet)
    print("🏆 | DONE! balance: ", bank, "| Max LOSE streak =", 
                          max_streak, " | Max Streak Count =", max_count)



def test(times):
 countH = 0 
 countT = 0
 for x in range(times):
    r = flipcoin()
    if r == "H":
        countH = countH + 1 
    if r == "T":
        countT = countT + 1
 print("Counts: H=",countH, " T:", countT)

#test() will test the randomness of this application      
#test(arg1)
bet(1000,arg1)

# stop the timeit
stop = timeit.default_timer()
print ('Time: ', '{0:.10f}'.format(stop - start))