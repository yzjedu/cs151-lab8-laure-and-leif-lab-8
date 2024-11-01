
import random

def calc_dice_sum():
    dice_sum = random.randint(2, 12)
    return dice_sum

def get_dice_sum_list(roll_number):
    count = 0
    dice_sum_list = []
    while count <= roll_number:
        dice_sum_list = [].append(calc_dice_sum())
        count += 1
    return dice_sum_list

def output_chart(roll_number, dice_sum_list):
    print('Rolling', roll_number, 'pairs of dice')
    print(dice_sum_list)
    print('Sum of 02:', '*'*dice_sum_list[0], '\nSum of 03:','*'*dice_sum_list[1], '\nSum of 04:','*'*dice_sum_list[2], '\nSum of 05:', '*'*dice_sum_list[3], '\nSum of 06:', '*'*dice_sum_list[4], '\nSum of 07:', '*'*dice_sum_list[5], '\nSum of 08:', '*'*dice_sum_list[6], '\nSum of 09:','*'*dice_sum_list[7], '\nSum of 10:','*'*dice_sum_list[8], '\nSum of 11:','*'*dice_sum_list[9], '\nSum of 12:', '*'*dice_sum_list[10])

def main():
    print('Welcome to the dice simulation program!')
    roll_number = int(input('How many times would you like to roll the pair of dice?'))
    while roll_number <= 0:
        roll_number = input('How many times would you like to roll the pair of dice?')
    calc_dice_sum()
    dice_sum_list = get_dice_sum_list(roll_number)
    output_chart(roll_number, dice_sum_list)

main()