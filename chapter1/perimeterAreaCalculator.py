def main():
    #ask user input for width and length
    width = input("Enter the width for the rectangle: ")
    #Start loop
    while True:
        try:
            width = int(width)
            if width < 1 or width > 100:
                print("The width is invalid.")
                width = input("Please enter an value between 1 and 100: ")
            else:
                break

        except ValueError:
            print("The width has to be an integer")
            width = input("Enter a new width for the rectangle: ")

    length = input("Enter the length for the rectangle: ")
    while True:
            try:
                length = int(length)
                if length < 1 or length > 100:
                    print("The length is invalid.")
                    length = input("Please enter an value between 1 and 100: ")
                else:
                    break
    
            except ValueError:
                print("The length has to be an integer")
                length = input("Enter a new length for the rectangle: ")

    area = width * length
    perimeter = (2 * width) + (2 * length)

    print(f"Area of the rectangle:\n{area}\nPerimeter of the rectangle:\n{perimeter}")

main()





