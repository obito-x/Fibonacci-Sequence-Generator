# find_Euler_number.py
# {obito}

"""

'This program is the generator of e(euler number) with nth decimal place like earlier program pi generator.'

Like Pi this also
:
advantage  : if you(user) enter other input instead of number , no effect on this program.

disadvantage: program output materials form is depend on the size of your(user's) terminal.

But don't worry. even the view is not clear , this program can work exactly
 
                
recommend: [ 81 x 24  ]
use this ratio on your terminal and run this program.
And view clearly.
    

    enjoy :)


-Obito-



"""

from colorama import Fore

# variable
ch = 'y'


# Factorial generator
def facto(m):
    m = int(m)

    def factorial(k):
        if k == 0:
            return 1
        else:
            return k * (factorial(k - 1))

    if type(m) == float:
        print('Type error')
    elif m < 0:
        return factorial(m * (-1)) * (-1)
    else:
        return factorial(m)


# summation of e
def summation_of_e(end, start=0):
    sub = 0
    for i in range(start, 1 + end):
        sub += (1 / facto(i))
    return sub


while ch == 'y':
    print('\n' * 10)  # Space

    print(Fore.GREEN + '\n' + '+' * 60 + '\n')
    print(
        Fore.BLUE + '\n' + ' This program is the generator of ' + Fore.GREEN + 'e' + Fore.BLUE
        + ' with nth decimal ' + 'place ' + '\n ' + Fore.RESET)  # Title
    print(Fore.GREEN + '\n' + '+' * 60 + '\n')

    print('\n' * 8)  # Space

    print(Fore.RED + '\nWarning:' + Fore.YELLOW + 'The Maximum: 50!!\n'
          + ' ' * 8 + 'Only whole numbers of decimal place can enter!\n' + ' ' * 8 + 'eg: 0,4,23,50\n'
          + Fore.RESET)  # Warning
    try:
        n = int(input(Fore.CYAN + "\nEnter the nth decimal place of e: " + Fore.GREEN))
    except:
        continue
    # user input and error handling

    if n < 51:
        try:
            print(Fore.CYAN + '\ne: ' + Fore.RESET +
                  f'%1.{n}f' % summation_of_e(99))
        except:
            continue
        # if user enter negative values, this error handling can fix
        # Generate Less than 51
    if n > 50:
        print(Fore.CYAN + '\ne: ' + Fore.RESET + '%1.51f' % summation_of_e(99))
        print(Fore.LIGHTRED_EX + "\nThis generator can't generate after 51th." + Fore.RESET)
        # Generate greater than 50
    ch = input(Fore.GREEN + '\nEnter {-y-} to do again: ' + Fore.RESET)  # ask do again

    print('\n' * 4)  # Spacey
