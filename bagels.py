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

def ask_for_input():
    guess = input("Please enter your guess ")
    return guess


def valid_input(guess):
    validity = False
    if guess.isnumeric() == False:
        print("Please enter a number!")
        return validity 
    if len(guess) != len(the_secret_number):
        print("Your guess must be a " + str(len(the_secret_number)) +"-digit number.")
        return validity 
    if guess[0] == "0":
        print("There must be no leading zeros.")
        return validity 
    list_of_digits = []
    list_without_duplicates = []
    list_of_duplicates = []
    for d in guess:
        list_of_digits.append(d)
        list_of_digits.sort()
        #print("This is list of digits ", list_of_digits)
    for d1 in list_of_digits:
        #print(d1)
        if d1 not in list_without_duplicates:
            list_without_duplicates.append(d1)
            #print (list_without_duplicates)
        else:
            list_of_duplicates.append(d1)
            #print (list_of_duplicates)
    #print("This is list of duplicates ", list_of_duplicates)
    #print("This is list without duplicates ", list_without_duplicates)        
    if list_of_duplicates != []:
        print("Your guess must not have repeated numbers.")
        return validity
    for i in guess:
        if i not in list_of_numbers:
            print("Your guess must have digits that are in the following list:", list_of_numbers)
            return validity        
    validity = True 
    return validity
    #check if the digits are in the list of numbers

def bagels():
    guess = ask_for_input()
    validity = valid_input(guess) 
    while validity == False:
        guess = ask_for_input()
        validity = valid_input(guess)
    #use list_of_guess_digits 
    while guess != the_secret_number:        
        fermi = 0
        pico = 0
        for k in guess:
            if (k in the_secret_number) and (guess.index(k) == the_secret_number.index(k)):
                    fermi = fermi + 1
            elif (k in the_secret_number) and (guess.index(k) != the_secret_number.index(k)):
                    pico = pico + 1
        print(pico * "Pico ", end = "")
        print(fermi * "Fermi ", end = "")
        if (fermi == 0) and (pico == 0):
            print("Bagels", end = " ")
        if (guess.index(k) + 1) == len(the_secret_number):
            print() #go to a new line before asking the user for a different guess  
        guess = ask_for_input()
        validity = valid_input(guess)
        while validity == False:
            guess = ask_for_input()
            validity = valid_input(guess)
    print("Congrats, your guess is correct!")  

if __name__=="__main__":
    bagels()