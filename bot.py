from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import logging
import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def search_planet(bot, update):
    user_text = update.message.text.split()
    print(user_text)
    d = ephem.now()
    planets = {'Mars':ephem.Mars, 
               'Mercury':ephem.Mercury,
               'Venus':ephem.Venus,
               'Jupiter':ephem.Jupiter,
               'Saturn':ephem.Saturn,
               'Uranus':ephem.Uranus,
               'Neptune':ephem.Neptune}
    if len(user_text) == 2:
        if user_text[1] in planets:
            d = ephem.now()
            planet = planets[user_text[1]](d)
            answer = ephem.constellation(planet)
            update.message.reply_text(answer[1])
        else:
            update.message.reply_text('Планета не найдена!')
    else:
        update.message.reply_text('Допускается название только одной планеты!')

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", search_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()

main()