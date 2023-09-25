#%% 
# # Coin Flip Streaks
# For this exercise, we’ll try doing an experiment. 
# If you flip a coin 100 times and write down an “H” for each heads and “T” for each tails, you’ll create a list that looks like “T T T T H H H H T T.” 
# If you ask a human to make up 100 random coin flips, you’ll probably end up with alternating head-tail results like “H T H T H H T H T T,” which looks random (to humans), 
# but isn’t mathematically random. 
# A human will almost never write down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips. 
# Humans are predictably bad at being random.
# 
# 

#%% 
# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. 
# # Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, 
# and the second part checks if there is a streak in it. 
# Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. 
# As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.
# You can start with the following template:
# 

#%%
import random
number_of_streaks = 0


for experiment_number in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flip_list = []
    for _ in range(100):                            # I read somewhere that using underscore for variables used in loops that aren't in use is the norm
        coin_flip = random.randint(0,1)
        flip_list.append(coin_flip)
        

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 1                                      # Start the streak variable at 1. This is because once the 'coin' is flipped, that starts the streak
    for i in range(len(flip_list)):                 # for loop that loops for the number of values in the list. Ie. 100
        if flip_list[i] == flip_list[i-1]:
            streak += 1
        else:                                       
            streak = 1                              # if the flip doesn't equal the previous flip, reset the streak to 1
        #print(streak)                              # Added this line to understand how the script loop worked. Remove the hash to see workings
        if streak == 6:
            number_of_streaks += 1
            break                                   # Once the 
    # The above was code was inspired by https://codereview.stackexchange.com/questions/275130/coin-flip-streaks-in-python
    #print(flip_list)                               # Added this line to understand how the script loop worked. Remove the hash to see workings
print('Chance of streak: %s%%' % (number_of_streaks / 100))

