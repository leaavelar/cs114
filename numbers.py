print('Pick number between 1 and 99.')
num = int(input())
tens = num//10
ones = num%10
if ones == 1:
    one_word = 'one'
elif ones == 2:
