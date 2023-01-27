import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types


token = '5591978168:AAH7W0Jwl4oFAHdtgYbh_hwTG5lMocWCO-U'
bot = telebot.TeleBot(token)




URL = 'https://kaktus.media/?lable=8&date=2023-01-26&order=time'
def get_html(url):
    response = requests.get(url)
    return response.text

def get_title(html):
    soup = BeautifulSoup(html,'lxml')
    titles = soup.find_all('div',class_='Tag--article')
    data_titles={}
    data=[]
    for title in titles:
        main_title = title.find('a',class_='ArticleItem--name').text.lstrip('\n')
        link_title = title.find('a',class_='ArticleItem--name').get('href')
        data_titles = {'number':titles.index(title)+1,'title':main_title,'link':link_title}
        data.append(data_titles)
    new_data = data[0:20]
    return new_data

news = get_title(get_html(URL))


inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
inline_button = types.InlineKeyboardButton(news[0]['title'],callback_data='1')
inline_button1 = types.InlineKeyboardButton(news[1]['title'],callback_data='2')
inline_button2= types.InlineKeyboardButton(news[2]['title'],callback_data='3')
inline_button3= types.InlineKeyboardButton(news[3]['title'],callback_data='4')
inline_button4= types.InlineKeyboardButton(news[4]['title'],callback_data='5')
inline_button5= types.InlineKeyboardButton(news[5]['title'],callback_data='6')
inline_button6= types.InlineKeyboardButton(news[6]['title'],callback_data='7')
inline_button7= types.InlineKeyboardButton(news[7]['title'],callback_data='8')
inline_button8= types.InlineKeyboardButton(news[8]['title'],callback_data='9')
inline_button9= types.InlineKeyboardButton(news[9]['title'],callback_data='10')
inline_button10= types.InlineKeyboardButton(news[10]['title'],callback_data='11')
inline_button11 = types.InlineKeyboardButton(news[11]['title'],callback_data='12')
inline_button12 = types.InlineKeyboardButton(news[12]['title'],callback_data='13')
inline_button13 = types.InlineKeyboardButton(news[13]['title'],callback_data='14')
inline_button14 = types.InlineKeyboardButton(news[14]['title'],callback_data='15')
inline_button15 = types.InlineKeyboardButton(news[15]['title'],callback_data='16')
inline_button16 = types.InlineKeyboardButton(news[16]['title'],callback_data='17')
inline_button17 = types.InlineKeyboardButton(news[17]['title'],callback_data='18')
inline_button18 = types.InlineKeyboardButton(news[18]['title'],callback_data='19')
inline_button19 = types.InlineKeyboardButton(news[19]['title'],callback_data='20')
inline_keyboard.add(inline_button,inline_button1,inline_button2,inline_button3,inline_button4,inline_button5,inline_button6,inline_button7,inline_button8,inline_button9,
inline_button10, inline_button11,inline_button12,inline_button13,inline_button14,inline_button15,inline_button16,inline_button17,inline_button18,inline_button19)

@bot.message_handler(commands=['start','hi'])
def start_message(message: types.Message):
    # print(message)
    bot.send_message(message.chat.id, 'Новости', reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == '1':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[0]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[0]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()
        elif call.data == '2':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[1]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[1]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()
        elif call.data == '3':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[2]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[2]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()                
        elif call.data == '4':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[3]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[3]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()
        elif call.data == '5':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[4]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[4]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()
        elif call.data == '6':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[5]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[5]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()
        elif call.data == '7':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[6]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[6]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()
        elif call.data == '8':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[7]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[7]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()

        elif call.data == '9':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[8]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[8]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()

        elif call.data == '10':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[9]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[9]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()

        elif call.data == '11':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[10]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[10]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()
        elif call.data == '12':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[11]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[11]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()
        elif call.data == '13':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[12]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[12]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()                
        elif call.data == '14':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[13]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[13]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()
        elif call.data == '15':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[14]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[14]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()
        elif call.data == '16':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[15]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[15]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()
        elif call.data == '17':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[16]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[16]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()
        elif call.data == '18':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[17]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[17]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()

        elif call.data == '19':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[18]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[18]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()

        elif call.data == '20':
            inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
            button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
            button2 = types.InlineKeyboardButton("Подробнее", url=news[19]['link'])
            inline_keyboard.add(button2, button)
            bot.send_message(call.message.chat.id, news[19]['link'],reply_markup=inline_keyboard)
            
            @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
            def stop_command(message):
                bot.send_message(callback.message.chat.id, 'Досвидания!')
                bot.stop_polling()
bot.polling()