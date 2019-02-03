def simple_bagels():
    the_secret_number = "123"
    guess = input("Please enter your guess ")
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
        guess = input("Please enter your guess ")        
    print("Congrats, your guess is correct!")
    

if __name__=="__main__":
    simple_bagels()