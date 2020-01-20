from random import randint


def generate_sequence(difficulty):
    gen_list = []
    for i in range(0, difficulty):
        gen_list.append(randint(1, 101))
    return gen_list


def get_list_from_user(difficulty):
    user_list = []
    print("\n----------------\n")
    print("Hello and welcome to MemoryGame")
    print(f"Please enter a {difficulty} random numbers")
    for i in range(0, difficulty):
        user_list.append(int(input()))

    return user_list


def is_list_equal(list1, list2):
    count = 0
    for i in range(1, len(list(list1))):
        if list1[i] != list2[i]:
            count = count + 1
    if count > 0:
        return False
    else:
        return True


def play(difficulty):
    gen_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    is_equal = is_list_equal(gen_list, user_list)
    return is_equal
