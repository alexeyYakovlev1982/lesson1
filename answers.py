import re

################ get_answer ##################
#def get_answer(key, dictionary):
#    return dictionary[re.sub( r'[^\w]', ' ',key).lower().strip()] 

def get_answer(key, dictionary):
    return dictionary.get(re.sub( r'[^\w]', ' ',key).lower().strip(), "Hmmmmmmm.....")

################ MAIN ##################
if __name__ == '__main__':
    answers_dict = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    print(get_answer(input("Enter the key: "), answers_dict))

