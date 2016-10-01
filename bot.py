from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import answers

def start(bot, update):
    print ("Вызван /start")
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

############## count ########################

def count(bot, update):
    print ("Вызван /count")
    answer_text = 'Количество слов=' + str(count_words(update.message.text) - 1)
    print ('/count ' + answer_text)
    bot.sendMessage(update.message.chat_id, text=answer_text)


def count_words(message):
    return len(message.split())


############## /count2 ########################

def count2(bot, update):
    print ("Вызван /count2")
    bot.sendMessage(update.message.chat_id, text='Количество слов=' + str(len(update.message.text[7:]).split()))



############## talk_to_me ########################

def talk_to_me(bot, update):
    print('Пришло сообщение: %s' % update.message.text)
    bot.sendMessage( update.message.chat_id, answers.get_answer(update.message.text, answers.answers_dict) )


###################### MAIN ################################

def main():
    updater = Updater("246802878:AAGL7HFqKYQ0gBaXiaYe2lRF6gVOJYPVJmw")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("count", count))
    dp.add_handler(CommandHandler("count2", count))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    