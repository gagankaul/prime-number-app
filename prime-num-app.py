import time

print("Welcome to the Prime Number App")

state = True
while state:

    #Get user input
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    choice = input("Enter your choice 1 or 2: ")

    #Determine if a number is prime
    if choice == "1":
        num = int(input("Enter a number to determine if it is prime or not: "))
        
        #Prime status check
        prime_status = True
        if num!= 1:
            for i in range(2,num):
                if num % i == 0:
                    prime_status = False
                    break
        else:
            prime_status = False

        if prime_status == True:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")    
    
    #Finding prime numbers within a range of numbers and time the calculations
    elif choice == "2":
        lower = int(input("Enter the lower bound of your range: "))
        upper = int(input("Enter the upper bound of your range: "))

        primes = []

        #Get the current time
        start_time = time.time()

        #Check prime status of all numbers between lower and upper bounds
        for num in range(lower, upper):
            if num > 1:
                prime_status = True
                for i in range (2, num):
                    if num % i == 0:
                        prime_status = False
                        break
            else:
                prime_status = False

            if prime_status == True:
                    primes.append(num)
        
        #Get the current time
        end_time = time.time()
        
        #Determine the total time elapsed
        elapsed_time = end_time - start_time
        print(f"\nIt took {elapsed_time} seconds to complete this calculation.")
        print(f"The following numbers between {lower} and {upper} are prime:")
        input("Press enter to continue.")
        
        #Display all numbers in the primes list
        for each in primes:
            print(each)
    
    #Not a valid choice entered by the user
    else:
        print("This is not a valid option.")

    #Ask user if they would like to play again
    play_again = input("Would you like to run the program again (y/n): ")
    if play_again != "y":
        state = False
        print("\nThank you for using this program. Have a nice day!")