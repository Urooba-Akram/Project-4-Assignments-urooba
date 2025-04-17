def main():
    # Step 1: Create a list of fruits
    fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Step 2: Print the length of the list
    lst_length = len(fruit_lst)
    print(f"The length of the fruit list is: {lst_length}")

    # Step 3: Add 'mango' at the end of the list
    fruit_lst.append('mango')

    # Step 4: Print the updated list
    print("Updated list of fruits:")
    for fruit in fruit_lst:
        print(fruit)

if __name__ == '__main__':
    main()
