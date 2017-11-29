import random

def get_input():
    print("Magic 8 ball")

    print("Hello what is your name?")
    name = input()
    print("Ask me a question and I will tell your fortune.")
    question = input()


    def get_input():
        name = input()
    return name

def get_random_num():
    random_num = random.randint(1, 9)
    return random_num

def get_question(random_num):
    if random_num == 1:
        return "No"
    elif random_num == 2:
        return "Yes"
    elif random_num == 3:
        return "Maybe"
    elif random_num == 4:
        return "Ask tomorrow"
    elif random_num == 5:
        return "Does not look good"
    elif random_num == 7:
        return "Ask again in three years"
    elif random_num == 8:
        return "Very doubtful"
    elif random_num == 9:
        return "Concetrate and ask again"

# def make_message():
#     get_question = input()
#     return


#     user's name with the fortune


# fortune = question(random_num)
# print (fortune)

def main():
    name = get_input()
    random_num = get_random_num()
    fortune = get_question(random_num)
    # message = get_message(name, fortune)
    print(fortune)
main()
