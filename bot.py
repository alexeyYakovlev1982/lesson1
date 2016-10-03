
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import answers

literal_numbers = ('ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять')

def start(bot, update):
    print ("Вызван /start")
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

############## count ########################

def count(bot, update):
    print ("Вызван /count")
    answer_text = 'Количество слов {}'.format( str( count_words(update.message.text)-1 ) )
    print ('/count ' + answer_text)
    bot.sendMessage(update.message.chat_id, text=answer_text)


def count_words(message):
    return len(message.split())


############## /count2 ########################

def count2(bot, update):
    print ("Вызван /count2")
    bot.sendMessage(update.message.chat_id, text='Количество слов {}'.format( str(  len( update.message.text[7:].split() ) )  ) )


############## /calc ################

def calc(bot, update):
    print ("Вызван /calc")
    if update.message.text.strip()[-1:] != '=':
        bot.sendMessage(update.message.chat_id, 'Последний элемент должен быть = ')
        return
    else:
        bot.sendMessage(update.message.chat_id, 'Рeзультат = {}'.format( str( math_calc (update.message.text.strip()[5:-1].strip()) ) ) )


############## /litercalc ################

def litercalc(bot, update):
    print ("Вызван /litercalc")
    message_words = update.message.text.lower().strip()[10:].split()
    print (message_words)

    if message_words[0] == 'сколько' and message_words[1] == 'будет':
        bot.sendMessage(update.message.chat_id, 'Вычисление: {}'.format(message_words[2:]))
        message_words.remove('сколько')
        message_words.remove('будет')
        if 'плюс' in message_words: 
            action = '+'
            message_words.remove('плюс')
        if 'минус' in message_words: 
            action = '-'
            message_words.remove('минус')
        if 'умножить' in message_words: 
            action = '*'
            message_words.remove('умножить')
        if 'разделить' in message_words: 
            action = '/'
            message_words.remove('разделить')
        message_words.remove('на')
        math_result = math_calc('{}{}{}'.format( literal_numbers.index(message_words[0]),action,literal_numbers.index(message_words[1]) ) ) 
        bot.sendMessage(update.message.chat_id, '{} = {}'.format( update.message.text[10:], math_result))
    else:
        bot.sendMessage(update.message.chat_id, 'Cannot find "сколько будет".')




############## math_calc #######################

def math_calc(math_expression):

    math_result = 0

    if '+' in math_expression:
        math_result = int( math_element_nnvl( math_expression.split('+')[0] ) ) + int( math_element_nnvl( math_expression.split('+')[1] ) )

    if '-' in math_expression:
        math_result = int( math_element_nnvl( math_expression.split('-')[0] ) ) - int( math_element_nnvl( math_expression.split('-')[1] ) )

    if '*' in math_expression:
        math_result = int( math_element_nnvl( math_expression.split('*')[0] ) ) * int( math_element_nnvl( math_expression.split('*')[1] ) )

    if '/' in math_expression:
        if int(math_expression.split('/')[1]) == 0:
            print ('Деление на 0 недопустимо!')
            #bot.sendMessage(update.message.chat_id, 'Деление на 0 недопустимо!')
            return ('Деление на 0 недопустимо!')
        else:    
            math_result = int( math_element_nnvl( math_expression.split('/')[0] ) ) / int( math_element_nnvl( math_expression.split('/')[1] ) )
    
    return math_result

def math_element_nnvl(element):
    try: 
        return float(element)
    except:
        return 0

############## talk_to_me ########################



def talk_to_me(bot, update):
    print( 'Пришло сообщение: {}'.format(update.message.text) )
    bot.sendMessage( update.message.chat_id, answers.get_answer(update.message.text, answers.answers_dict) )
    print( 'last element is {}'.format( update.message.text.strip()[-1:] ) )
     

    if update.message.text.strip()[-1:] == '=':
        bot.sendMessage( update.message.chat_id, 'Вычисление: {}{}'.format( update.message.text.strip(), str( math_calc(update.message.text.strip()[:-1]) ) ) )


###################### MAIN ################################

def main():
    updater = Updater("246802878:AAGL7HFqKYQ0gBaXiaYe2lRF6gVOJYPVJmw")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("count", count))
    dp.add_handler(CommandHandler("count2", count2))
    dp.add_handler(CommandHandler("calc", calc))
    dp.add_handler(CommandHandler("litercalc", litercalc))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    
