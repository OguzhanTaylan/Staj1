from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import commands as c

     
TOKEN = "5782286885:AAGIiJkcWQqRr68mToB187hs604j1JYDaoc"

print("Bot çalışmaya başladı!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", c.start_command))
    dp.add_handler(CommandHandler("Haberler",  c.get_news))
    dp.add_handler(CommandHandler("Yaskawa",  c.yaskawa_news))
    dp.add_handler(CommandHandler("Stajyerler", c.stajyer))
    dp.add_handler(CommandHandler("KitapBul", c.getBook))
    dp.add_handler(CommandHandler("HavaDurumu", c.getWeather))
    dp.add_handler(CommandHandler("GuncelKur", c.getCurrencies))

 
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()