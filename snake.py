import random

def roll_dice():
    return random.randint(1, 6)

def move_player(player, steps):
    player += steps
    if player > 100:
        player = 100 - (player - 100) 
    return player

def check_snake_or_ladder(position):
    snakes_and_ladders = {
        4: 14, 9: 31, 17: 7, 20: 38, 28: 84, 40: 59,
        51: 67, 54: 34, 62: 19, 63: 81, 64: 60, 71: 91,
        87: 24, 93: 73, 95: 75, 99: 78
    }
    return snakes_and_ladders.get(position, position)

def main():
    player_position = 0

    while player_position < 100:
        input("Press Enter to roll the dice")
        steps = roll_dice()
        print("You rolled a", steps)
        player_position = move_player(player_position, steps)
        player_position = check_snake_or_ladder(player_position)
        print("You are now at position", player_position)

    print("Congratulations You won!")

if __name__ == "__main__":
    main()
