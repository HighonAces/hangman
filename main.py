from tinydb import TinyDB, Query
import random

db = TinyDB('sample.json')


def main():
    print("1. Start a new game\n2. Insert a word\n3. Check the list of words\n")
    x = int(input("Please select one of the above\t"))
    if x == 1:
        new_game()
    elif x == 2:
        insert_word()
    elif x == 3:
        list_all_words()
    else:
        print("Please select a valid entry")
    main()


def list_all_words():
    print(db.all())


def insert_word():
    word = str(input("Enter a word\t"))
    clue = str(input("Enter a clue\t"))
    size = len(db) + 1

    db.insert({'id': size,
               'word': word,
               'clue': clue})


def new_game():
    size = len(db)
    num = random.randint(1, size)
    print("The clue is\n")
    dict1 = db.search(Query().id == num)
    print(dict1[0]["clue"])
    word = dict1[0]["word"]
    word_list = list(word)
    i: int
    for i in range(0, len(word)):
        print("_\t", end='')
    print("\n")
    print(
        f"The total number of letters is {len(word)}, so you will get {int(len(word) / 2)} wrong attempts to guess "
        f"the word right")
    attempts = int(len(word) / 2)
    # continue_game(attempts, word_list, word_list_new)
    while attempts:
        letter = str(input("Please enter your letter:\t"))
        c = word_list.count(letter)
        word_list_new = [None] * len(word_list)
        if c > 0:
            for i in range(0, len(word_list)):
                if letter == word_list[i]:
                    word_list_new[i] = word_list[i]
                else:
                    word_list_new[i] = "_"
            string_new = ''.join(map(str, word_list_new))
            print("The letter exists in the word")
            print(string_new)
            continue_game(attempts, word_list, word_list_new)
        else:
            print("The letter that you guessed is wrong")
            print(f"You have {attempts - 1} attempts left")
            attempts = attempts - 1
            continue_game(attempts, word_list)
    else:
        print("Pack your backpack, GAME OVER!!!")
        exit(0)


def continue_game(attempts, word_list, word_list_new=None):
    if word_list_new == word_list:
        print("YAYYY!!! The word you guessed is right")
        exit(0)
    elif attempts == 0:
        print("Pack your bags, GAME OVER!!!")
        exit(0)
    else:
        letter = str(input("Please enter your next letter:\t"))
        c = word_list.count(letter)
        if c > 0:
            for i in range(0, len(word_list)):
                if letter == word_list[i]:
                    word_list_new[i] = letter
            string_new = ''.join(map(str, word_list_new))
            print(string_new)
            print(f"your attempts = {attempts}")
            continue_game(attempts, word_list, word_list_new)
        else:
            print("The letter that you guessed is wrong")
            print(f"You have {attempts - 1} attempts left")
            attempts = attempts - 1
            continue_game(attempts, word_list, word_list_new)


main()
