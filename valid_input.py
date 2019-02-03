the_secret_number = "345"

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
    #for i in guess:
        #if i not in list_of_numbers:
            #print("Your guess must have digits that are in the following list", list_of_numbers)
            #return validity        
    #validity = True 
    return validity
    #check if the digits are in the list of numbers

if __name__ == "__main__":
    print(valid_input())
