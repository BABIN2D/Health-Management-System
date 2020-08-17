import datetime
def gettime():
    '''Time Function To Get The Current Time'''
    return datetime.datetime.now()
choice = input('Enter R to read\nEnter L to log\t')         # Decision on whether to write or read the txt file.

if choice in('L','l'):                                      # Entering the log or write function.
    user_name = input('Enter Your Name\t')                  # Asking the User to Enter There Name

    with open('Health Management System.txt','a') as file:  # Opening the Health Management System txt. file.
        file.write('Time-\t')
        file.write(str(gettime()))                          # Writing the time from the time function.
        file.write('\n')
        file.write('Name- ')
        file.write(user_name +'\n')                         # Writing the username
        diet_Exercise = input('Enter D for Diet\nEnter E for Exercise\t') # Decision on Diet or Exercise.

        if diet_Exercise in ('D','d'):
            file.write('Diet- ')
            while True:                                     # Entering in a while loop till the user wants to write
                                                            # his/her diet chart.
                file.write(input('Enter Your Diet\t')+'\t')      # Asking the user to input the diet.
                choice1 = input('Do You Want to Log More Diet?\t')  # decision box for more diet

                if choice1 in ('Yes','yes','YES','y','Y'):  # if the user enters any of the following - yes, Yes, YES,
                    continue                                # Y or y. this will count as the user wants to write more diet

                else:
                    file.write('\n')
                    print('Good Bye')
                    break                                   # Terminating the program if the above options are not in the list.

        elif diet_Exercise in('E','e'):                     # Entering exercise loop if user enters E or e.
            file.write('Exercise- ')
            while True:                                     # Entering the while loop
                file.write(input('Enter Your Exercise\t')+'\t')  # Asking user to input his/her exercise
                choice2 = input('Do You Want to Log More Exercise?\t') # Asking user if he/she wants to log more exercise.

                if choice2 in ('Yes','yes','YES','y','Y'):  # If user wants to log more exercise.
                    continue
                else:
                    file.write('\n')
                    print('Good Bye')
                    break                                   # If the user doesn't wish to log any more entries.
else:
    with open('Health Management System.txt') as fileR:
        print(fileR.read())
