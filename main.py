import random
import string
pass_length=int(input(f"Please enter the length you would your password to be: "))
pass_special=input(f"Please enter if you want to include special characters i.e. %, $, #, etc (enter Y or N): ")
pass_num=input(f"Please enter if you want to include numbers (enter Y or N): ")

letters = string.ascii_letters
special_char = string.punctuation     # "!@#$%^&*, etc."
numbers = string.digits               # "0123456789"
char_pool=letters

if pass_special.upper() == 'Y':
    char_pool+=special_char

if pass_num.upper() == "Y":
    char_pool+=numbers
    

def pass_generator():
    pass_list=[]
    for _ in range(pass_length):
        pass_list.append(random.choice(char_pool))
    return "".join(pass_list)



password=pass_generator()
print(f"Your password is {password}")