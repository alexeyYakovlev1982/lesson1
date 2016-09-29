from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import answers

def start(bot, update):
	print ("Вызван /start")
	bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def talk_to_me(bot, update):
    print('Пришло сообщение: %s' % update.message.text)
    #bot.sendMessage(update.message.chat_id, update.message.text)
    bot.sendMessage( update.message.chat_id, answers.get_answer(update.message.text, answers.answers_dict) )
	

def main():
    updater = Updater("246802878:AAGL7HFqKYQ0gBaXiaYe2lRF6gVOJYPVJmw")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    