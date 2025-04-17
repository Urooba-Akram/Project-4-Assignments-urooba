#Problem Statement
#Write a program to solve this age-related riddle!

#Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

#Anton is 21 years old.

#Beth is 6 years older than Anton.

#Chen is 20 years older than Beth.

#Drew is as old as Chen's age plus Anton's age.

#Ethan is the same age as Chen.

#Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):

#Anton is 3

#Beth is 4

#Chen is 5

#Drew is 6

#Ethan is 7

def main():
    # Anton's age is given
    anton_age = 21
    
    # Beth is 6 years older than Anton
    beth_age = anton_age + 6
    
    # Chen is 20 years older than Beth
    chen_age = beth_age + 20
    
    # Drew is as old as Chen's age plus Anton's age
    drew_age = chen_age + anton_age
    
    # Ethan is the same age as Chen
    ethan_age = chen_age
    
    # Print each person's name and age
    print("Anton is " + str(anton_age))
    print("Beth is " + str(beth_age))
    print("Chen is " + str(chen_age))
    print("Drew is " + str(drew_age))
    print("Ethan is " + str(ethan_age))

# This line is required to run the main function
if __name__ == '__main__':
    main()