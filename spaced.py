import random
import sys

player = {
'HP': 100,
'attack': 100,
'defense': 50,
'name': 'Player 1'
}

enemy1 = {
'HP': 100,
'attack': 50,
'defense': 80,
'name': 'Vampire'
}

enemy2 = {
'HP': 30,
'attack': 50,
'defense': 70,
'name': 'Monster'
}

enemy3 = {
'HP': 50,
'attack': 50,
'defense': 50,
'name': 'Evil Cat'
}


def game_over(player):
    print("GAME OVER -- ", player['name'], "You are dead.")
    return sys.exit()


def get_item(player):
    item_list = ["star dust", "lucky pen",]

    print("You found a", item_list[random.randint(0, 1)], "your health increased by",
    (abs(player['HP'] - 100)), "HP")
    player['HP'] += (abs(player['HP'] - 100))
    return player


def attack(opponent):
    rand_damage = random.randint(8, 32)
    opponent['HP'] -= rand_damage
    print(rand_damage, " damage!")
    return opponent


def fight(oppo1, oppo2):
    while (oppo1['HP'] > 0) and (oppo2['HP'] > 0):
        print(oppo1['name'], " attacks ", oppo2['name'])
        attack(oppo2)
        if oppo2['HP'] <= 0:
            print(oppo1['name'], " is winner")
        else:
            print(oppo2['name'], " attacks ", oppo1['name'])
            attack(oppo1)
        if oppo1['HP'] <= 0:
            print(oppo2['name'], " is winner")
            game_over(oppo1)
    print('player oppo1 HP: ', oppo1['HP'])
    print('enemy1  oppo2 HP: ', oppo2['HP'])


def encounter(player, opponent):
    if player['HP'] > 70:
        fight(player, opponent)
        input('Press any key to continue')
    elif opponent['name'] == 'Vampire':
        fight(player, opponent)
    else:
        get_item(player)
        input('Press any key to continue')


def main():
   
    print('encounter 1.\n\n')
    encounter(player, enemy3)
    print('encounter 2.\n\n')
    encounter(player, enemy2)
    print('encounter 3.\n\n')
    encounter(player, enemy1)
    print("You have escaped -- WINNER", player['name'], " HP: ", player['HP'])


if __name__ == "__main__":
 
    main()
