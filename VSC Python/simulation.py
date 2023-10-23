import math


rightletters= { " ":[1.5,-4], "y":[-2,2], "u":[-1,2], "i":[0,2], "o":[1,2], "p":[2,2], "h":[-1.5,0], "j":[-0.5,0], "k":[0.5,0], "l":[-1.5,0], "b":[-1.5,-2], "n":[-0.5,-2], "m":[-0.5,-2], "v":[-2.5,-2]}
leftletters = {" ":[-1.5,-4], 'q':[-2, 2], 'w':[-1,2],"e": [0,2], "r": [1,2], "t": [2,2], "a": [-1.5, 0], "s": [-0.5,0], "d":[0.5,0], "f": [1.5,0],"g": [2.5, 0], "z": [-0.5, -2], "x": [0.5, -2], "c": [1.5,-2] }

right_handed= []
left_handed = []
with open('tweets.txt', 'r') as f:
    lines = f.readlines()


for each_line in lines:
    word_list = each_line.split()
    
    for each_word in word_list:
        for each_letter in each_word:
            if each_letter in rightletters.keys():
                right_handed.append(each_letter)

            if each_letter in leftletters.keys():
                left_handed.append(each_letter)
       
        left_handed.append(" ")
        right_handed.append(" ")

right_lenghts = 0
left_lenghts = 0

ram_x = 666
ram_y = 666
right_x= 0
right_y = 0
left_x = 0
left_y = 0

for letter in right_handed:
    if ram_x == 666:
        ram_x= rightletters[letter][0] 
    
    elif ram_x != 666:
        right_x = (rightletters[letter][0] - ram_x)**2

    if ram_y == 666:
        ram_y= rightletters[letter][0] 
    
    elif ram_y != 666:
        right_y = (rightletters[letter][0] - ram_y)**2
    
    a = math.sqrt(right_x + right_y)
    right_lenghts += a


for letter in left_handed:
    if ram_x == 666:
        ram_x= leftletters[letter][0] 
    
    elif ram_x != 666:
        left_x = (leftletters[letter][0] - ram_x)**2

    if ram_y == 666:
        ram_y= leftletters[letter][0] 
    
    elif ram_y != 666:
        left_y = (leftletters[letter][0] - ram_y)**2
    
    a = math.sqrt(left_x + left_y)
    left_lenghts += a

total_lenghts= right_lenghts + left_lenghts
print(format(total_lenghts, ".2f"))