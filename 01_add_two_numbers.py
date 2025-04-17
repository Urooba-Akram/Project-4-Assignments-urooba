def main():
    # Step 1: User se pehla number lena
    print("This program adds two numbers.")
    
    # Step 2: Pehla number input karna aur integer mein convert karna
    num1 = int(input("Enter first number: "))
    
    # Step 3: Doosra number input karna aur integer mein convert karna
    num2 = int(input("Enter second number: "))
    
    # Step 4: Dono numbers ka sum calculate karna
    total = num1 + num2
    
    # Step 5: Result print karna
    print("The total is " + str(total) + ".")

# Is line ki zarurat hai taake main function run ho sake
if __name__ == '__main__':
    main()

    