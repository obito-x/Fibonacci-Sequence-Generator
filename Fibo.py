#  fibo.py
#  {obito}

from colorama import Fore

#       colors

g = Fore.GREEN
r = Fore.RED
b = Fore.BLUE
rs = Fore.RESET
y = Fore.YELLOW
c = Fore.CYAN


print('\n'*50)
print(c + """
                                        
                                        1
                                    1       1
                                1       2       1
                            1       3       3       1
                        1       4       6       4       1
                    1       5       10      10      5       1
                1       6       15      20      15      6       1
            1       7       21      35      35      21      7       1
        1       8       28      56      70      56      28      8       1
    1       9       36      84      126     126     84      36      9       1
 """+ y + """+++++++++++++++++++++++++++++++"""+ b + """[Fiboncci Sequence]"""+ y +"""+++++++++++++++++++++++++++++                     

     """)

print(b + '_'*10 + ' '*12 + '_'*10 + ' ')
e = int(input(b + '_'*10 + c +'Enter number' + b + '_'*10 + '\n|\n|__/' + g + '==' + c + '[ '))

def fibonacci(num):
    f1 = 1
    f2 = 0
    for i in range(num):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        yield f3

txtfile = lambda lam: open('result.txt', f'{lam}')

tt = txtfile('w')
ii = [1,1,0]
for item in fibonacci(e):

    if ii[0] > ii[1]*10:
        tt.write('\n')
        ii[1] += 1
    tt.write(str(item) + ' , ')
    ii[0] += 1
print('\n' + '__'*40)
print('\n' + g)

tt = txtfile('r')

tt.seek(0)
while ii[2] < e/10:
    print(tt.readline())
    ii[2] += 1
print(Fore.YELLOW + '\n\n' + ' '*10 + 'Done!\n')
print(' '*10 + 'Save to result.txt\n' + c + '__'*40 + Fore.RESET + '\n\n')


