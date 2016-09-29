import re
answers_dict = { "привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся", "когда на работу":"завтра", "ты мне надоел":"не бросай меня!" }

################ get_answer ##################

def get_answer(key, dictionary):
    return dictionary.get(re.sub( r'[^\w]', ' ',key).lower().strip(), "Hmmmmmmm.....")

################ ask_user ##################
def ask_user():
    #while input("How r u? :") != "Good": pass
    while True:
        try:
            user_input = input("Say smth: ")
            print( get_answer(user_input, answers_dict ))
            if get_answer(user_input, answers_dict ) == "Увидимся" : break
        except (KeyboardInterrupt, EOFError):
            print ("\nКак жаль, что вы нас покидаете....")
            break

################ MAIN ##################
if __name__ == '__main__':
    
    #print(get_answer(input("Enter the key: "), answers_dict))
    ask_user()
