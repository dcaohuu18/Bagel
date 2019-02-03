import random 

def user_choices(): 
    print("How many different digits would you like to use?")
    range_of_number = int(input("Please enter a number that is equal to or smaller than 10 and greater than 1: "))
    while range_of_number > 10 or range_of_number <= 1:
        range_of_number = int(input("Please enter a number that is equal to or smaller than 10 and greater than 1: "))    
    number_of_digits = int(input("How many digits long should the number be? Please enter a number that is smaller than or equal to " + str(range_of_number) + " and greater than 1: "))
    while (number_of_digits > range_of_number) or (number_of_digits) <= 1:
        number_of_digits = int(input("Please enter a number that is smaller than or equal to " + str(range_of_number) + " and greater than 1: "))
    list_of_numbers = []
    for i in range(range_of_number):
        list_of_numbers.append(str(i))
    print("Your guess must have digits that are in the following list:", list_of_numbers)
    return number_of_digits, list_of_numbers

number_of_digits, list_of_numbers = user_choices()
#print(list_of_numbers)
    
def secret_number():
    the_secret_number = ""
    copy_of_list_of_numbers = []
    for i in list_of_numbers:
        copy_of_list_of_numbers.append(i) 
    for j in range(number_of_digits):
        if j == 0:
            copy_of_list_of_numbers.remove("0")
            random_choice = random.choice(copy_of_list_of_numbers) 
            the_secret_number = the_secret_number + random_choice
            copy_of_list_of_numbers.remove(random_choice)
            copy_of_list_of_numbers.append("0")
            copy_of_list_of_numbers.sort()
        else:
            random_choice = random.choice(copy_of_list_of_numbers)
            the_secret_number = the_secret_number + random_choice
            copy_of_list_of_numbers.remove(random_choice)
    return the_secret_number   

the_secret_number = secret_number()
print(the_secret_number)
    
if __name__ == "__main__":
    secret_number()