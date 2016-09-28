import answers

names_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]	
answers_dict = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

################ find_person ##################
def find_person(name):
    while names_list:
        if names_list.pop() == name:
            print (name + " нашелся")
            break


################ ask_user ##################
def ask_user():
    #while input("How r u? :") != "Good": pass
    while True:
        try:
            user_input = input("Say smth: ")
            print( answers.get_answer(user_input, answers_dict ))
            if answers.get_answer(user_input, answers_dict ) == "Увидимся" : break
        except KeyboardInterrupt:
            print ("\nКак жаль, что вы нас покидаете....")
            break


################ MAIN ##################
if __name__ == '__main__':
    #find_person("Валера")
    ask_user()

