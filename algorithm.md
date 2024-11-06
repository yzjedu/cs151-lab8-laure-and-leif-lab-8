# Algorithm Document


* Purpose: Simulates rolling two dice and finding the sum
* Name: calc_dice_sum
* Params: none
* Return: dice_sum
* Algorithm:
1. create the variable dice_1 and set it equal to a random integer between 1 and 6
2. create the variable dice_2 and set it equal to a random integer between 1 and 6
3. create the variable dice_sum and set it equal to dice_1 and dice_2 added together
4. return dice_sum

-----------------------

* Purpose: creates a list that holds the sum of each dice roll and how many times a certain sum is rolled
* Name: get_dice_sum_list
* Params: roll_number
* Return: dice_sum_list
* Algorithm:
1. set variable count equal to 0
2. initialize the list dice_sum_list with 11 values of 0 as a placeholder
3. while variable count is less than or equal to the value of variable roll_number
   1. call function calc_dice_sum and set it equal to variable dice_sum
   2. find the value in dice_sum_list with index of dice_sum - 2, and add 1 to its current value
   3. add 1 to the value of variable count
4. return dice_sum_list

-------------------------

* Purpose: displays the results of the dice rolls to the user as a chart of asterisks
* Name: output_chart
* Params: roll_number, dice_sum_list
* Return: none
* Algorithm:
1. output "Rolling (roll_number) pairs of dice to the user
2. output the value of dice_sum_list
3. output a chart similar to the one below using asterixes to represent the value of each index of the dice_sum_list list
```python 
Sum of 02 **
Sum of 03 ********
Sum of 04 ***********
Sum of 05 ***********
Sum of 06 ***************
Sum of 07 ***************
Sum of 08 *****************
Sum of 09 *********
Sum of 10 *******
Sum of 11 ****
Sum of 12 *   
```
-------------------
* Purpose: main function
* Name: main
* Params: none
* Return: none
* Algorithm: 
1. Output "Welcome to the dice simulation program!" to the user
2. create the variable roll_number and set it equal to user input, given the prompt "How many times would you like to roll the pair of dice as an integer?"
3. while the value of roll_number is less than or equal to 0
   1. set the variable roll_number equal to user input, given the prompt "How many times would you like to roll the pair of dice as an integer?"
4. call function calc_dice_sum
5. call function get_dice_sum_list and set it equal to the variable dice_sum_list
6. call function output_chart 
7. output to the user, "Thank you for using this program!"

-----------------------------------------