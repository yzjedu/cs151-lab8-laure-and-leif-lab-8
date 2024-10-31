# Algorithm Document


* Purpose: fetching the number of rolls from the user
* Name: "roll_fetch"
* Parameters: none
* Return: the number of rolls the program should execute
* Algorithm:
1. Global import "roll_count"
2. Set a boolean variable, "passthru," equal to False
3. while "passthru" is false:
   1. Request the user input the number of dice rolls they want
   2. Set variable "roll_count" equal to the aforementioned input 
   3. if "roll_count" is not a digit:
        1. output an error message to the user, explaining it must be a positive whole number
   4. otherwise
        1. output a confirmation message with the number of dice rolls
      2. set "passthru" to True

* Purpose: finding the tallies for the possible dice sums (2-11)
* Name: "roll_tallying"
* Parameters: none
* Return: a completed list of dice sums
* Algorithm:
1. Global import "roll_count"
2. Global import "roll_list"
3. set a variable, "current_count," equal to zero
4. while "current_count" is less than "roll_count":
    1. set a variable, "roll1," equal to a random number between 1 and 6
   2. set a variable, "roll2," equal to a random number between 1 and 6
   3. set a variable, "roll," equal to the sum of "roll1" and "roll2"
   4. Add 1 to the list position equal to "roll"
   5. Add 1 to "current_count"

* Purpose: Executing functions and outputing results to user
* Name: "main"
* Parameters: none
* Return: outputted tally of rolls to the user
* Algorithm:
1. Set a variable, "roll_count," equal to an empty string
2. Create an empty list called "roll_list"
3. execute "roll_fetch"
4. execute "roll_tallying"
5. output the results from "roll_tallying" in the following format or similar:
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