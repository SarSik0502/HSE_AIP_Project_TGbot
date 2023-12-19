import requests
import telebot
from datetime import date
import datetime
from bs4 import BeautifulSoup
from telebot import types
bot = telebot.TeleBot('6428270782:AAEZyzWDS1VGNmNdujBOxE743EYvj8l_T5Q')
URL_STR = 'https://www.e-disclosure.ru/'
headers = {'User-Agent': 'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome / 114.0.0.0 Safari/537.36'}
full_page = requests.get(URL_STR, headers)
soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("a", {"target": "_blank"})
global n
n = 0
@bot.message_handler(commands = ['start'])
def main(message):
    """
    Start bot

    :param message: Text from user
    :type message: string
    :return: nothing
    """
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Получать новости")
    btn4 = types.KeyboardButton("Курсы акций")
    markup.row(btn1, btn4)
    btn2 = types.KeyboardButton("Курсы валют")
    btn3 = types.KeyboardButton("Курсы криптовалют")
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
def on_click(message):
    """
    Button processing

    :param message: Text from user
    :type message: string
    :return: if message == Курсы валют: Bot sends exchange rates
             if message == Получать новости: Bot sends news(without stopping)
             if message == Курсы криптовалют: Bot sends cryptocurrency rates
             if message == Курсы акций: Bot sends excise rates
    :rtype: string
    :raises if message != (Курсы валют, Получать новости, Курсы криптовалют, Курсы акций)
    """
    if message.text == "Курсы валют":
        current_date = str(date.today())
        s = "Курсы валют на " + current_date + ":" + "\n"
        URL_STR2 = 'https://cbr.ru/curreNcy_base/daily/'
        headers2 = {'User-Agent': 'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome / 114.0.0.0 Safari/537.36'}
        full_page = requests.get(URL_STR2, headers2)
        soup2 = BeautifulSoup(full_page.content, 'html.parser')
        convert2 = soup2.findAll("td")
        k = 3
        while k < 100:
            k += 5
            s1 = str(convert2[k])
            s2 = str(convert2[k + 1])
            s1 = s1[s1.find(">") + 1:s1.find("<", 2)]
            s2 = s2[s2.find(">") + 1:s2.find("<", 2)]
            s += s1 + " - " + s2 + "\n"
        bot.send_message(message.chat.id, s)
        s_restart = "Не забудь перезапустить бота /start"
        bot.send_message(message.chat.id, s_restart)
    elif message.text == "Получать новости":
        global n
        n += 1
        if n == 1:
            s_restart = "Вскоре новости начнут приходить, не забудь перезапустить бота /start"
            bot.send_message(message.chat.id, s_restart)
            i = 0
            while (True):
                headers = {
                    'User-Agent': 'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome / 114.0.0.0 Safari/537.36'}
                full_page = requests.get(URL_STR, headers)
                soup = BeautifulSoup(full_page.content, 'html.parser')
                convert = soup.findAll("a", {"target": "_blank"})
                if i == 0:
                    last_text = convert[2].text
                    last_name = convert[1].text
                i += 1
                if (last_text != convert[2].text or last_name != convert[1].text):
                    link = str(convert[1])
                    link = link[link.find('"') + 1: link.find('"', link.find('"') + 1)]
                    s = convert[1].text + "\n" + convert[2].text + "\n" + link
                    bot.send_message(message.chat.id, s)
                    last_text = convert[2].text
                    last_name = convert[1].text
        else:
            s = "Новости уже вам отправляются"
            bot.send_message(message.chat.id, s)
            s_restart = "Не забудь перезапустить бота /start"
            bot.send_message(message.chat.id, s_restart)
    elif message.text == "Курсы криптовалют":
        current_date = str(datetime.datetime.now())
        current_date = current_date[:-10]
        s = "Курсы криптовалют на " + current_date
        URL_STR3 = 'https://ru.investing.com/crypto/'
        headers3 = {'User-Agent': 'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome / 114.0.0.0 Safari/537.36'}
        full_page = requests.get(URL_STR3, headers3)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("td")
        for i in range(2, 70, 10):
            s += str(convert[i].text) + str(convert[i + 1].text) + str(convert[i + 2].text)
        bot.send_message(message.chat.id, s)
        s_restart = "Не забудь перезапустить бота /start"
        bot.send_message(message.chat.id, s_restart)
    elif message.text == "Курсы акций":
        current_date = str(datetime.datetime.now())
        current_date = current_date[:-10]
        s = "Курсы криптовалют на " + current_date + "\n"
        URL_STR4 = 'https://ru.investing.com/equities/'
        headers4 = {'User-Agent': 'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome / 114.0.0.0 Safari/537.36'}
        full_page = requests.get(URL_STR4, headers4)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("td")
        for i in range(1, 300, 10):
            s += str(convert[i].text) + " " + str(convert[i + 1].text) + " " + str(convert[i + 5].text) + "\n"
        bot.send_message(message.chat.id, s)
        s_restart = "Не забудь перезапустить бота /start"
        bot.send_message(message.chat.id, s_restart)
    else:
        s = "Для взаимодействя с ботом пользуйтесь встроенными кнопками"
        bot.send_message(message.chat.id, s)
        s_restart = "Не забудь перезапустить бота /start"
        bot.send_message(message.chat.id, s_restart)
bot.infinity_polling()

