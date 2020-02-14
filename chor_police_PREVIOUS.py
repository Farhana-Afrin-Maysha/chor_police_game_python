import random

def call_police():
    print('The index of Boss is: ', mylist.index(100))
    print('The index of Police is: ', mylist.index(80))
    y = int(input('Say the index no of thief. '))
    if (y == mylist.index(00)):
        print('You are correct')
    else:
        print('You are not correct')

msg = "Welcome to chor-police game"
print(msg)
nums = [00, 80, 60, 100]
random.shuffle(nums)
print(nums)
mylist = [n for n in nums]
player1 = mylist[0]
#
# mylist = remove.(mylist[0])
#
player2 = mylist[1]
player3 = mylist[2]
player4 = mylist[3]
#
print(player1)
# print(player2)
# print(player3)
# print(player4)
# arr = array('i', [])

x = int(input('Enter a value (from 0-3). '))
# for i in range(4):
#   x = int(input('Enter the next value (from 0-3). '))
#   arr.append(x)
#
# print(arr)

if (x <= 3):
    if (mylist[x] == 00):
        print(' You have got the "Thief = 00" card ')
        print(call_police())

    elif (mylist[x] == 80):
        print(' You have got the "Police = 80" card')
        print(call_police())

    elif (mylist[x] == 60):
        print(' You have got the "Robber = 60" card')
        print(call_police())

    elif (mylist[x] == 100):
        print(' Your have got the "Boss = 100" card')
        print(call_police())

else:
    print('Your input is not valid')
