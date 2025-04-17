def main():
    # User se number lena
    curr_value = int(input("Enter a number: "))

    # Jab tak value 100 se choti hai, tab tak loop chale
    while curr_value < 100:
        # Value ko double karna
        curr_value = curr_value * 2
        # Print karna
        print(curr_value)

# Main function call karna
if __name__ == '__main__':
    main()
