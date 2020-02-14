import random


def find_thief():
    y = int(input('Say the index no of thief. '))
    if (y == mylist.index(00)):
        print('You are correct')
    else:
        print('You are not correct')


def call_police():
    print("Info: The index of Boss  & Police is - ", mylist.index(100), mylist.index(80))
    local = mylist
    local.remove(100)
    local.remove(80)
    random.shuffle(local)
    print("Polic: The value of thief - ", local[0])
    if (local[0] == 60):
        print("Police is failure to catch the thief")
    else:
        print("Police have caught the thief")


msg = "Welcome to Thief-Police game"
msg1 = "Police: Hello everyone, I will catch the thief"
print(msg)
nums = [00, 80, 60, 100]
random.shuffle(nums)
print(nums)
mylist = [n for n in nums]

x = int(input('choose a card from (0-3). '))

player1 = mylist[x]
player2 = mylist[1]
player3 = mylist[2]
player4 = mylist[3]

print('player 1')
print('player 2')
print('player 3')
print('player 4')

for i in range(1):
    if (player1 == 00):
        print(' You have got the "Thief = 00" card ')
        print(msg1)
        print(call_police())

    elif (player1 == 80):
        print(' You have got the "Police = 80" card')
        print(find_thief())

    elif (player1 == 60):
        print(' You have got the "Robber = 60" card')
        print(msg1)
        print(call_police())

    elif (player1 == 100):
        print(' Your have got the "Boss = 100" card')
        print(msg1)
        print(call_police())
