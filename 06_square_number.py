#Problem Statement
#Ask the user for a number and print its square (the product of the number times itself).

#Here's a sample run of the program (user input is in bold italics):

#Type a number to see its square: 4

#4.0 squared is 16.0

def main():
    # Step 1: User se number lena
    number = float(input("Type a number to see its square: "))
    
    # Step 2: Square calculate karna
    square = number ** 2
    
    # Step 3: Square ka result print karna
    print(str(number) + " squared is " + str(square))

# This line is required to run the main function
if __name__ == '__main__':
    main()