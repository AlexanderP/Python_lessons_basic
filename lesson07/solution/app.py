from lesson07.solution.module import *

boxes = BoxIterator()

print("Loto game - v0.1 alpha\n\n")

username = input('Type username: ')

players = [
    Player(username, Card()),
    Player('computer', Card())
]


def looser(user: Player):
    print(f"User {user.name} loose!")
    quit()


def winner(user: Player):
    print(f"User {user.name} win!")
    quit()


def user_action(box_number: int):
    command = input("What You want to do? [N - Next / C - Check] ")[0].lower()
    user = players[0]

    if command == 'n':
        if user.card.is_number_exists(box_number):
            looser(user)
    elif command == 'c':
        if user.card.is_number_exists(box_number):
            user.card.check_number(box_number)

            if user.card.is_completed:
                winner(user)
        else:
            looser(user)
    else:
        print("Invalid command, try again!")
        user_action(box_number)


def computer_action(box_number: int):
    user = players[1]

    if user.card.is_number_exists(box_number):
        user.card.check_number(box_number)

        if user.card.is_completed:
            winner(user)


for box in boxes:
    print(players[0])
    print(players[1])

    print(f"\nBox number is ___{box}___")
    
    user_action(box)
    computer_action(box)
