import telebot
import urllib.request
from bs4 import BeautifulSoup

bot = telebot.TeleBot("508733841:AAEv-oQf1O-CMYsD5i7KEIFR6qtbDeQDfgQ")

@bot.message_handler(commands=['pikabupopular'])
def pikabu_best(message):
    output = ''
    html = urllib.request.urlopen('https://pikabu.ru/best/1').read()
    title = BeautifulSoup(html, 'html.parser').find_all('a', class_='story__title-link')
    i = 0
    for link in title:
        bot.send_message(message.chat.id,"https://pikabu.ru/" + link.get("href"))
        i +=1
        if i == 5:
            return

@bot.message_handler(commands=['pikabupopularone'])
def pikabu_best_one(message):
    output = ''
    html = urllib.request.urlopen('https://pikabu.ru/best/1').read()
    for link in BeautifulSoup(html, 'html.parser').find_all('a', class_='story__title-link'):
        output += (link.get("href") + '\n')
        break
    bot.send_message(message.chat.id, "https://pikabu.ru/" + output)

if __name__ == '__main__':
     bot.polling(none_stop=True)