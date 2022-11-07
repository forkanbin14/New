
import random

Lower_case = "abcdefghigklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
number = "01941528390"
symbol = "~!@#$%^&*+_:"

use_for = lower_case + upper_case + number + symbol
length_of_password = 9

password = "".join(random.sample(use_for, length _of_password))

print ("Your Generated Password is: ", password)
