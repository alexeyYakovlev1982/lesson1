
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#import answers
import ephem
import re
import datetime

import csv

import logging
#logging.basicConfig(level=logging.DEBUG)

from answers import get_answer, ask_user, liter_to_math_expression, math_calc, full_moon_calc, get_answer, cont_days_to_NY



literal_numbers = ('ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять')
answers_dict = { "привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся", "когда на работу":"завтра", "ты мне надоел":"не бросай меня!" }

log_file_name = 'bot_log_{}.csv'.format( datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S") )


############## start ########################

def start(bot, update):
    print ("Вызван /start")
    user_info = '{} {} {}'.format(update.message.from_user.id, update.message.from_user.first_name, update.message.from_user.last_name)
    logging_bot (user_info, update.message.text)
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')
    logging_bot (bot.getMe().username, 'Давай общаться')


############## count ########################

def count(bot, update):
    print ("Вызван /count")
    user_info = '{} {} {}'.format(update.message.from_user.id, update.message.from_user.first_name, update.message.from_user.last_name)
    logging_bot (user_info, update.message.text) 

    answer_text = 'Количество слов {}'.format( str( count_words(update.message.text)-1 ) )
    print ('/count ' + answer_text)
    bot.sendMessage(update.message.chat_id, text=answer_text)
    logging_bot (bot.getMe().username, answer_text)

def count_words(message):
    return len(message.split())


############## /count2 ########################

def count2(bot, update):
    print ("Вызван /count2")
    user_info = '{} {} {}'.format(update.message.from_user.id, update.message.from_user.first_name, update.message.from_user.last_name)
    logging_bot (user_info, update.message.text)
    answer = 'Количество слов {}'.format( str(  len( update.message.text[7:].split() ) )  ) 

    bot.sendMessage(update.message.chat_id, answer)
    logging_bot (bot.getMe().username, answer)

############## /calc ################

def calc(bot, update):
    print ("Вызван /calc")
    user_info = '{} {} {}'.format(update.message.from_user.id, update.message.from_user.first_name, update.message.from_user.last_name)
    logging_bot (user_info, update.message.text)
    if update.message.text.strip()[-1:] != '=':
        answer = 'Последний элемент должен быть = '
    else:
        answer = 'Рeзультат = {}'.format( str( math_calc (update.message.text.strip()[5:-1].strip()) ) ) 

    bot.sendMessage(update.message.chat_id, answer)
    logging_bot (bot.getMe().username, answer)


############## /litercalc ################

def litercalc(bot, update):
    print ("Вызван /litercalc")
    user_info = '{} {} {}'.format(update.message.from_user.id, update.message.from_user.first_name, update.message.from_user.last_name)
    logging_bot (user_info, update.message.text)
    message_words = update.message.text.lower().strip()[10:].split()
    #print (message_words)

    if message_words[0] == 'сколько' and message_words[1] == 'будет':
        math_result = math_calc (liter_to_math_expression(update.message.text[10:]))
        answer = str(math_result)
    else:
        answer = 'Cannot find "сколько будет".'
    bot.sendMessage(update.message.chat_id, answer)
    logging_bot (bot.getMe().username, answer)


############## /NY ################

def NY(bot, update):
    print ("Вызван /NY")
    user_info = '{} {} {}'.format(update.message.from_user.id, update.message.from_user.first_name, update.message.from_user.last_name)
    logging_bot (user_info, update.message.text)
    date_text = update.message.text.strip()[3:].strip()
    #print (date_text)
    if '-' in date_text:
        date_text_separ = date_text.split('-')
    elif '/' in date_text:
        date_text_separ = date_text.split('/')
    #print (date_text_separ)
    initial_date = datetime.date(int(date_text_separ[0]), int(date_text_separ[1]), int(date_text_separ[2]))
    #print (initial_date)
    answer = 'До нового года {}'.format(cont_days_to_NY(initial_date) )
    print (answer)
    
    bot.sendMessage(update.message.chat_id, answer)
    logging_bot (bot.getMe().username, answer)


############## logging_bot ########################

def logging_bot(username = '', message = ''):
    cur_date = datetime.datetime.strftime(datetime.datetime.now(), "%Y.%m.%d")
    cur_time = datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S.%f")
    csv_write_list = [cur_date, cur_time, username, message]

    with open(log_file_name, 'a', newline='') as csv_log_file:
        csv_log_writer = csv.writer(csv_log_file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_log_writer.writerow(csv_write_list)

    #with open( log_file_name, 'a', encoding='utf-8' ) as log_file:

    #    print('{}|{}|{}|{}'.format(cur_date, cur_time, username, message), file=log_file)


############## talk_to_me ########################

def talk_to_me(bot, update):
    print( 'Пришло сообщение: {}'.format(update.message.text) )
    print( 'last element is {}'.format( update.message.text.strip()[-1:] ) )
    print( 'first element is {}'.format( update.message.text.strip().split()[0] ) )
    
    user_info = '{} {} {}'.format(update.message.from_user.id, update.message.from_user.first_name, update.message.from_user.last_name)
    logging_bot (user_info, update.message.text) 
    
    answer = get_answer(update.message.text)
    bot.sendMessage( update.message.chat_id, answer )
    
    #print ('user is {} {} {}'.format(update.message.from_user.id, update.message.from_user.first_name, update.message.from_user.last_name))
    #print (bot.getMe().username)
    #print ('{}|{}|{} {}|{}'.format(str(datetime.strftime(datetime.now(), "%Y.%m.%d")), str(datetime.strftime(datetime.now(), "%H:%M:%S.%f")), update.message.from_user.first_name, update.message.from_user.last_name, update.message.text)
    #print ('{}|{}'.format( datetime.datetime.strftime(datetime.datetime.now(), "%Y.%m.%d"), datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S.%f") ) )
    logging_bot (bot.getMe().username, answer)
    
###################### MAIN ################################

def main():
    updater = Updater("246802878:AAGL7HFqKYQ0gBaXiaYe2lRF6gVOJYPVJmw")
    

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("count", count))
    dp.add_handler(CommandHandler("count2", count2))
    dp.add_handler(CommandHandler("calc", calc))
    dp.add_handler(CommandHandler("litercalc", litercalc))
    dp.add_handler(CommandHandler("NY", NY))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    
