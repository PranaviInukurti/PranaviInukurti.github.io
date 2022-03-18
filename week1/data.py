# Menu options in print statement
def print_menu1():
    print('1 -- Red')
    print('2 -- Orange')
    print('3 -- Yellow')
    print('4 -- Green')
    print('5 -- Blue')
    print('6 -- Purple')
    print('7 -- Pink')
    print('8 -- Black')
    print('9 -- Exit')


# menu option 1
def red():
    print('You chose \' 1 -  Red\'')


# menu option 2
def orange():
    print('You chose \' 2 - Orange\'')


# menu option 3
def yellow():
    print('You chose \'3 - Yellow\'')


# menu option 4
def green():
    print('You chose \' 4 -  Green\'')


# menu option 5
def blue():
    print('You chose \' 5 -  Blue\'')


# menu option 6
def purple():
    print('You chose \' 6 -  Purple\'')


# menu option 7
def pink():
    print('You chose \' 7 -  Pink\'')


# menu option 8
def black():
    print('You chose \' 8 -  Black\'')


def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-4: '))
            if option == 1:
                red()
            elif option == 2:
                orange()
            elif option == 3:
                yellow()
            elif option == 4:
                green()
            elif option == 5:
                blue()
            elif option == 6:
                purple()
            elif option == 7:
                pink()
            elif option == 8:
                black()
            # Exit menu
            elif option == 9:
                print('Exiting! Thank you! Good Bye...')
                exit()  # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')


runOptions()

# Menu options as a dictionary
menu_options = {
    1: 'Red',
    2: 'Orange',
    3: 'Yellow',
    4: 'Green',
    5: 'Blue',
    6: 'Purple',
    7: 'Pink',
    8: 'Black',
    9: 'Exit',
}


# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])
    runOptions()


if __name__ == '__main__':
    # print_menu1()
    print_menu2()

