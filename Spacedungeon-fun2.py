print('Hello')
print("Welcome to Space Dungeon")

def get_name():
    print('To begin please choose a character name.')
    name = input()
    return name

def get_character():
    print("Now pick a character type.")
    character = input()
    return character

def get_magic():
    print("You can only have a total of 100 magic and attack points combined.")
    print("How many magic points do you want?")
    magic = input()
    return magic

def get_attack ():
    print("How many attack points do you want?")
    attack = input()
    return attack

def main():
    name = get_name()
    character = get_character()
    magic = get_magic()
    attack = get_attack()

main ()

# print('Pick a character type')
# character = input()
# print('You can only have a total of 100 magic and attack points combined.')
# print('How many magic points do you want?')
# magic = input()
# print('How many attack points do you want?')
# attack = input()
# print("You have chosen the character name" , name , "and character type" , character , "you have", magic , "magic points and" , attack , 'attack points.' )
