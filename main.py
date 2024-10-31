
import random
def calc_roll_number():
    roll_number = input('How many times would you like to roll the pair of dice?')
    while not roll_number.isdigit():
        roll_number = input('How many times would you like to roll the pair of dice?')
    while roll_number <= 0:
        roll_number = input('How many times would you like to roll the pair of dice?')
    return roll_number

def calc_dice_sum():
    dice_sum = random.randint(2, 12)
    return dice_sum

def output_chart(dice_sum_list, roll_number):
    print('Rolling', roll_number, 'pairs of dice')
    print(dice_sum_list)
    print('Sum of 02', '*'*(dice_sum_list[0]), '\nSum of 03','*'*(dice_sum_list[1]), '\nSum of 04','*'*(dice_sum_list[2]), '\nSum of 05', '*'*(dice_sum_list[3]), '\nSum of 06', '*'*(dice_sum_list[4]), '\nSum of 07', '*'*(dice_sum_list[5]), '\nSum of 08', '*'*(dice_sum_list[6]), '\nSum of 09','*'*(dice_sum_list[7]), '\nSum of 10','*'*(dice_sum_list[8]), '\nSum of 11','*'*(dice_sum_list[9]), '\nSum of 12')


def main(roll_number, dice_sum):
    count = 0
    print('Welcome to the dice simulation program!')
    calc_roll_number()
    dice_sum_list = ([])
    while count <= roll_number:
        calc_dice_sum()
        dice_sum_list.append(dice_sum)
        count += 1
    dice_sum_list.sort()
    output_chart(dice_sum_list, roll_number)
