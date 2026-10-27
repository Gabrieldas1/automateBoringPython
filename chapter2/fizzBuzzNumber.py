#accept int from user
#if int % 3 == 0 program prints Fizz
#if int % 5 == 0 program prints Buzz
#if int is divisible by both, print Fizz Buzz
#else programs pring the input.

def main():
    user_number = input("Enter an integer: ")
    while True:
        if user_number == "q":
            return False
        try:
            user_number = int(user_number)
            if user_number < 1 or user_number >= 100:
                print("Your number has to be positive and lower than 100")
                user_number = input("Enter your new integer: ")
            else:
                break
        except ValueError:
            print("Your number has to be an integer")
            user_number = input("Enter your new integer: ")
    if user_number % 3 == 0 and user_number % 5 == 0:
        print("Fizz Buzz")
    elif user_number % 3 == 0:
        print("Fizz")
    elif user_number % 5 == 0:
        print("Buzz")
    else:
        print(user_number)
main()
