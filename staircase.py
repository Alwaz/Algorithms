''' input n = 4
   #
  ##
 ###
####              '''

def stairCase(n):
    for i in range(n):
        for spaces in range(n-i-1):#  loop to print spaces
            print(' ', end='')
        for j in range(i+1):
            print('#', end='')
        print()



steps = int(input('Enter steps: '))
stairCase(steps)



