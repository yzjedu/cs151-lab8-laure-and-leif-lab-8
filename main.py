# Programmers: Laure Patera, Leif Labianca
# Course: CS151, Dr. Zee
# Due Date: 11/7/24
# Programming Assignment: Lab 08
# Problem Statement: Program shows distribution of results of dice rolls
# Data In: number of times the user wishes to roll the dice
# Data Out: chart of sums of dice rolls
# Credits: readme file and examples shown in class

import random

#Purpose: Simulates rolling two dice and finding the sum
#Name: calc_dice_sum
#Params: none
#Return: dice_sum as an integer, represents the sum of dice from one simulated roll
def calc_dice_sum():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_sum = dice_1 + dice_2
    return dice_sum

#Purpose: creates a list that holds the sum of each dice roll and how many times a certain sum is rolled
#Name: get_dice_sum_list
#Params: roll_number (makes sure the list stores the right number of values)
#Return: dice_sum_list as a list, represents the number of times a certain sum was rolled
def get_dice_sum_list(roll_number):
    count = 0
    dice_sum_list = [0] * 11
    while count <= roll_number:
        dice_sum = calc_dice_sum()

        #tracks the number of times that a certain dice sum is rolled
        dice_sum_list[dice_sum - 2] +=1

        count += 1
    return dice_sum_list

#Purpose: displays the results of the dice rolls to the user as a chart of asterisks
#Name: output_chart
#Params: roll_number (tells the user how many times the dice was rolled), dice_sum_list (allows data from this list to be accessed and turned into a chart)
#Return: none
def output_chart(roll_number, dice_sum_list):
    print('Rolling', roll_number, 'pairs of dice')
    print(dice_sum_list)
    print('Sum of 02:', '*'*dice_sum_list[0], '\nSum of 03:','*'*dice_sum_list[1], '\nSum of 04:','*'*dice_sum_list[2], '\nSum of 05:', '*'*dice_sum_list[3], '\nSum of 06:', '*'*dice_sum_list[4], '\nSum of 07:', '*'*dice_sum_list[5], '\nSum of 08:', '*'*dice_sum_list[6], '\nSum of 09:','*'*dice_sum_list[7], '\nSum of 10:','*'*dice_sum_list[8], '\nSum of 11:','*'*dice_sum_list[9], '\nSum of 12:', '*'*dice_sum_list[10])

#Purpose: main function
#Name: main
#Params: none
#Return: none
def main():
    passthru = False

    print('Welcome to the dice simulation program!')

    # finds the number of times the user would like to roll the dice
    while not passthru:
        roll_number = input('How many times would you like to roll the pair of dice as an integer?')
        if not roll_number.isdigit():
            print('This is an invalid input. Your answer must be a positive whole digit')
        else:
            roll_number = int(roll_number)
            passthru = True

    #call function to simulate dice rolls
    calc_dice_sum()

    #call function to create a list that will store the results of each dice roll
    dice_sum_list = get_dice_sum_list(roll_number)

    #call function to display results to user as a chart
    output_chart(roll_number, dice_sum_list)

    #exit message
    print('Thank you for using this program!')

main()