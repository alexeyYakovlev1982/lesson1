import re
import datetime
import ephem
answers_dict = { "привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся", "когда на работу":"завтра", "ты мне надоел":"не бросай меня!" }


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


############## liter_to_math_expression #######################

def liter_to_math_expression(liter_expression):
    #print ('liter exp {}'.format(liter_expression))
    words = liter_expression.lower().strip().strip('?').split()
    words.remove('сколько')
    words.remove('будет')
    print (words)
    if 'плюс' in words: 
        action = '+'
        words.remove('плюс')
    if 'минус' in words: 
        action = '-'
        words.remove('минус')
    if 'умножить' in words: 
        action = '*'
        words.remove('умножить')
    if 'разделить' in words: 
        action = '/'
        words.remove('разделить')
    if 'на' in words: words.remove('на')


    if words[1] == 'и':
        element1 = literal_numbers.index(words[0]) + literal_numbers.index(words[2])*0.1
    else:
        print ('нет и')
        element1 = literal_numbers.index(words[0])
    print ('element1 = {}'.format(element1))

    if words[-2:][0] == 'и':
        element2 = literal_numbers.index(words[-3:][0]) + literal_numbers.index(words[-1:][0])*0.1
    else:
        print ('нет и - 2')
        element2 = literal_numbers.index(words[-1:][0])
    print ('element2 = {}'.format(element2))

    #print ('{}{}{}'.format( literal_numbers.index(words[0]),action,literal_numbers.index(words[1])))

    #return '{}{}{}'.format( literal_numbers.index(words[0]),action,literal_numbers.index(words[1]) )
    print ('{}{}{}'.format( element1, action, element2 ))
    return '{}{}{}'.format( element1, action, element2 )


############## math_calc #######################

def math_calc(math_expression):

    math_result = 0

    if '+' in math_expression:
        math_result = float( math_element_nnvl( math_expression.split('+')[0] ) ) + float( math_element_nnvl( math_expression.split('+')[1] ) )

    if '-' in math_expression:
        math_result = float( math_element_nnvl( math_expression.split('-')[0] ) ) - float( math_element_nnvl( math_expression.split('-')[1] ) )

    if '*' in math_expression:
        math_result = float( math_element_nnvl( math_expression.split('*')[0] ) ) * float( math_element_nnvl( math_expression.split('*')[1] ) )

    if '/' in math_expression:
        if float(math_expression.split('/')[1]) == 0:
            print ('Деление на 0 недопустимо!')
            return ('Деление на 0 недопустимо!')
        else:    
            math_result = float( math_element_nnvl( math_expression.split('/')[0] ) ) / float( math_element_nnvl( math_expression.split('/')[1] ) )
    
    return math_result

def math_element_nnvl(element):
    try: 
        return float(element)
    except:
        return 0

        
############## full_moon_calc ####################

def full_moon_calc(full_moon_date):
    return ephem.next_full_moon(full_moon_date)

############## mysql_answer ####################
def mysql_answer(request):
    Connection = pymysql.connect(host='localhost', user='bot', password='telebot', db='bot',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor )
#	cur = Connection.cursor()
#	cur.execute("SELECT * FROM distionary")
#	for response in cur:
#    	print(response)
#    	cur.close()
#	Connection.close()


############# cont_days_to_NY ####################
def cont_days_to_NY(initial_date = datetime.date.today()):
    answer = str( (datetime.date(initial_date.year +1, 1, 1) - initial_date).days)
    
    if answer[-1:] == '1':
        answer += ' день.'
    elif answer[-1:] == '2' or answer[-1:] == '3' or answer[-1:] == '4':
        answer += ' дня.'
    else: answer += ' дней.'
    
    return answer

############# cont_days_to_date ####################
def cont_days_to_date(dest_date):
    if '-' in dest_date:
        dest_date = dest_date.split('-')
    elif '/' in dest_date:
        dest_date = dest_date.split('/')
    print(dest_date)
    answer = str( (datetime.date(int(dest_date[0]), int(dest_date[1]), int(dest_date[2])) - datetime.date.today()).days)  

    if answer[-1:] == '1':
        answer += ' день.'
    elif answer[-1:] == '2' or answer[-1:] == '3' or answer[-1:] == '4':
        answer += ' дня.'
    else: answer += ' дней.'
    
    return answer 


    
############## get_answer ########################

def get_answer(request):
    
    if request.strip()[-1:] == '=':
        answer = ' {}{}'.format( request.strip(), str( math_calc(request.strip()[:-1]) ) ) 
    elif request.lower().strip().split()[0] == 'сколько' and request.lower().strip().split()[1] == 'будет':
        answer = math_calc(liter_to_math_expression(request)) 
    elif 'когда ближайшее полнолуние после' in request.lower():
        print (ephem.next_full_moon( request.lower().strip().strip('?').split()[-1:][0] ))
        answer = str(ephem.next_full_moon( request.lower().strip().strip('?').split()[-1:][0] ) )
    elif 'сколько дней осталось до нового года' in request.lower():
        print ('До нового года {}'.format(cont_days_to_NY() ))
        answer = 'До нового года {}'.format(cont_days_to_NY())
    elif 'сколько дней осталось до 2' in request.lower():
        dest_date = request.strip().strip('?').lower().split()[-1:][0]
        print ('До {} осталось {}'.format(dest_date, cont_days_to_date(dest_date)))
        answer = 'До {} осталось {}'.format(dest_date, cont_days_to_date(dest_date))
    else:
        answer = answers_dict.get(re.sub( r'[^\w]', ' ',request).lower().strip(), "Hmmmmmmm.....")
    
    print ('request is {}'.format(request))
    print ('answer is {}'.format(answer))
    
    return answer

################ MAIN ##################
if __name__ == '__main__':
    
    #print(get_answer(input("Enter the key: "), answers_dict))
    ask_user()
