#Change this to change the character of the drawing.
circle = "O"
#define funcition main
def main():
    #asks user input in str type
    width = input("Enter the width for the rectangle: ")
    #create while loop to check if the values are correct
    while True:
        #First try to turn the input to int, if values are not inside parameter, ask again.
        try:
            #transforms the width in int
            width = int(width)
            #parameters for if statement no less than 1, no more than 10.
            if width < 1 or width > 10:
                print("Those values are out of parameter, try again.")
                width = input("Enter the width for the rectangle: ")
            else:
                break
            #Value error aks input again 
        except ValueError:
            print("Width must be an integer")
            width = input("Enter the width for the rectangle: ")
            #cicle repeats till values are correct.
    
    line_of_circles = circle * width
    print(f"{line_of_circles}\n" * 5)

main() 