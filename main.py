
# import telebot
# from telebot import types
#
# import config
# bot = telebot.TeleBot(config.token)
#
# @bot.message_handler(commands = ['start'])
# def start_message(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
#     but1 = types.KeyboardButton('Русский')
#     but2 = types.KeyboardButton('English')
#     markup.add(but1,but2)
#     bot.send_message(message.chat.id,text = 'Выберите язык/Choose your language', reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text in ['Русский', 'English'])
# def handle_language(message):
#     global language
#     language = message.text
#     if language == 'Русский':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         but1 = types.KeyboardButton('Пхукет')
#         but2 = types.KeyboardButton('Бангкок')
#         but3 = types.KeyboardButton('Чангмай')
#         but4 = types.KeyboardButton('Вернутся в главное меню')
#         markup.add(but1,but2,but3,but4)
#
#     else:
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         but1 = types.KeyboardButton('Phuket')
#         but2 = types.KeyboardButton('Bangkok')
#         but3 = types.KeyboardButton('Changmai')
#         but4 = types.KeyboardButton('Back to main menu')
#         markup.add(but4, but1, but2,but3)
#
#     if language == 'Русский':
#         bot.send_message(message.chat.id,'Где вы находитесь?',reply_markup=markup)
#
#     elif message.text == 'Вернуться в главное меню' or message.text == 'Back to main menu':
#         start_message(message)
#
#     elif language == 'English':
#         bot.send_message(message.chat.id, 'Where are you located??',reply_markup=markup)
#
#
#
#
#
#
# @bot.message_handler(func=lambda message: message.text in ['Phuket','Bangkok','Changmai','Пхукет','Бангкок','Чангмай'])
# def handle_location(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     global place
#     place = message.text
#     if language == 'Русский':
#
#         but7 = types.KeyboardButton('Отель')
#         but8 = types.KeyboardButton('Пляж')
#         but9 = types.KeyboardButton('Кафе')
#         buthome = types.KeyboardButton('Вернутся в главное меню')
#         markup.add(but7, but8, but9,buthome)
#
#     elif language == 'English':
#
#         but10 = types.KeyboardButton('Hotel')
#         but11 = types.KeyboardButton('Beach')
#         but12 = types.KeyboardButton('Cafe')
#         buthome = types.KeyboardButton('Вернутся в главное меню')
#         markup.add(but10, but11, but12,buthome)
#
#     elif message.text == 'Back to main menu' or 'Вернутся в главное меню':
#         start_message(message)
#     if language == 'Русский':
#         bot.send_message(message.chat.id, text='Что вас интересует?', reply_markup=markup)
#     elif language == 'English':
#         bot.send_message(message.chat.id, text='What are you interested in?', reply_markup=markup)
#
# @bot.message_handler(func=lambda message: message.text in ['Пляж', 'Отель', 'Кафе', 'Beach', 'Hotel', 'Cafe'])
# def choose_place(message):
#
#     if message.text == 'Отель'and place == 'Пхукет':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.com/Hotel_Review-g297930-d13140255-Reviews-Hotel_Clover_Patong_Phuket-Patong_Kathu_Phuket.html')
#     elif message.text == 'Отель' and place == 'Бангкок':
#         bot.send_message(message.chat.id,text='https://www.tripadvisor.com/Hotel_Review-g293916-d13134217-Reviews-Akara_Hotel-Bangkok.html')
#     elif message.text == 'Отель' and  place == 'Чангмай':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.com/Hotel_Review-g293917-d7620257-Reviews-Akyra_Manor_Chiang_Mai-Chiang_Mai.html')
#     elif message.text == 'Пляж' and place == 'Пхукет':
#         bot.send_message(message.chat.id,text='https://www.tripadvisor.ru/Attraction_Review-g10804710-d450973-Reviews-or10-Karon_Beach-Karon_Beach_Karon_Phuket.html')
#     elif message.text == 'Пляж' and place == 'Бангкок':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Attraction_Review-g293919-d462836-Reviews-or25-Jomtien_Beach-Pattaya_Chonburi_Province.html')
#     elif message.text == 'Пляж' and place == 'Чангмай':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Attraction_Review-g3814839-d1746055-Reviews-Huai_Tueng_Thao-Don_Kaeo.html')
#     elif message.text == 'Кафе' and place == 'Пхукет':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.com/Hotel_Review-g297930-d13140255-Reviews-Hotel_Clover_Patong_Phuket-Patong_Kathu_Phuket.html')
#     elif message.text == 'Кафе' and place == 'Бангкок':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.com/Restaurant_Review-g293916-d12385615-Reviews-CharoenKrung_Cafe_Bar-Bangkok.html')
#     elif message.text == 'Кафе' and place == 'Чангмай':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.com.au/Restaurant_Review-g11879466-d12444872-Reviews-KOBQ_Korean_Barbecue_Restaurant-Su_Thep_Chiang_Mai.html')
#
#     elif message.text == 'Hotel' and place == 'Phuket':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.com/Hotel_Review-g297930-d13140255-Reviews-Hotel_Clover_Patong_Phuket-Patong_Kathu_Phuket.html')
#     elif message.text == 'Hotel' and place == 'Bangkok':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.com/Hotel_Review-g293916-d13134217-Reviews-Akara_Hotel-Bangkok.html')
#     elif message.text == 'Hotel' and place == 'Changmai':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.com/Hotel_Review-g293917-d7620257-Reviews-Akyra_Manor_Chiang_Mai-Chiang_Mai.html')
#     elif message.text == 'Beach' and place == 'Phuket':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Attraction_Review-g10804710-d450973-Reviews-or10-Karon_Beach-Karon_Beach_Karon_Phuket.html')
#     elif message.text == 'Beach' and place == 'Bangkok':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Attraction_Review-g293919-d462836-Reviews-or25-Jomtien_Beach-Pattaya_Chonburi_Province.html')
#     elif message.text == 'Beach' and place == 'Changmai':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Attraction_Review-g3814839-d1746055-Reviews-Huai_Tueng_Thao-Don_Kaeo.html')
#     elif message.text == 'Cafe' and place == 'Phuket':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.com/Hotel_Review-g297930-d13140255-Reviews-Hotel_Clover_Patong_Phuket-Patong_Kathu_Phuket.html')
#     elif message.text == 'Cafe' and place == 'Bangkok':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.com/Restaurant_Review-g293916-d12385615-Reviews-CharoenKrung_Cafe_Bar-Bangkok.html')
#     elif message.text == 'Cafe' and place == 'Changmai':
#         bot.send_message(message.chat.id, text='https://www.tripadvisor.com.au/Restaurant_Review-g11879466-d12444872-Reviews-KOBQ_Korean_Barbecue_Restaurant-Su_Thep_Chiang_Mai.html')
#
#
#
#
# if __name__ == '__main__':
#     bot.infinity_polling()


import telebot
from telebot import types

bot = telebot.TeleBot('7945405394:AAGXBTHOChhulbzR6F1uE7toT4gbJ74MItc')


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
    btn1 = types.KeyboardButton('Русский 🇷🇺')
    btn2 = types.KeyboardButton('English 🇬🇧')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text='Choose your language / Выберите язык', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ['Русский 🇷🇺', 'English 🇬🇧'])
def handle_language(message):
    global language
    language = message.text
    if language == 'Русский 🇷🇺':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пхукет')
        btn2 = types.KeyboardButton('Чангмай')
        btn3 = types.KeyboardButton('Бангкок')
        btn4 = types.KeyboardButton('Вернутся в главное меню')
        markup.add(btn1, btn2, btn3, btn4)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Phuket')
        btn2 = types.KeyboardButton('Chiang Mai')
        btn3 = types.KeyboardButton('Bangkok')
        btn4 = types.KeyboardButton('Back to main menu')
        markup.add(btn1, btn2, btn3, btn4)

    if language == 'Русский 🇷🇺':
        bot.send_message(message.chat.id, text='Где вы находитесь?', reply_markup=markup)

    elif message.text == 'Вернутся в главное меню' or message.text == 'Back to main menu':
        start_message(message)
    elif language == 'English 🇬🇧':
        bot.send_message(message.chat.id, text='Where are you located?', reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ['Phuket', 'Chiang Mai', 'Bangkok', 'Пхукет', 'Чангмай', 'Банкок', 'Back',
                                          'Назад'])
def handle_location(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    global place
    place = message.text
    if language == 'Русский 🇷🇺':
        btn1 = types.KeyboardButton('Пляж')
        btn2 = types.KeyboardButton('Кафе')
        btn3 = types.KeyboardButton('Отель')
        btn4 = types.KeyboardButton('Вернутся в главное меню')

        markup.add(btn1, btn2, btn3, btn4)
    elif language == 'English 🇬🇧':
        btn1 = types.KeyboardButton('Beach')
        btn2 = types.KeyboardButton('Cafes')
        btn3 = types.KeyboardButton('Hotel')
        btn4 = types.KeyboardButton('Back to main menu')
        markup.add(btn1, btn2, btn3, btn4)
    elif message.text == 'Вернутся в главное меню' or message.text == 'Back to main menu':
        start_message(message)

    if language == 'Русский 🇷🇺':
        bot.send_message(message.chat.id, text='Что вас интересует?', reply_markup=markup)
    elif language == 'English 🇬🇧':
        bot.send_message(message.chat.id, text='What are you interested in?', reply_markup=markup)

  
@bot.message_handler(
    func=lambda message: message.text in ['Пляж', 'Кафе', 'Отель', 'Beach', 'Cafes', 'Hotel', 'Back to main menu',
                                          'Вернутся в главное меню'])
def handle_interest(message):
    # ПЛЯЖ
    if message.text == 'Пляж' and place == "Пхукет":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Attraction_Review-g1210687-d450974-Reviews-Kata_Beach-Kata_Beach_Karon_Phuket.html')
    elif message.text == 'Пляж' and place == "Чангмай":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Hotel_Review-g293917-d17519162-Reviews-Riverside_Luxury_Pool_Villa_88_Place-Chiang_Mai.html')
    elif message.text == 'Пляж' and place == "Банкок":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Hotel_Review-g297916-d2644429-Reviews-Tamarina_Resort-Chonburi_Chonburi_Province.html')
    elif message.text == 'Вернутся в главное меню':
        start_message(message)
    # КАФЕ
    elif message.text == 'Кафе' and place == "Пхукет":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Restaurant_Review-g1215781-d25184563-Reviews-The_5th_Element_Phuket-Phuket_Town_Phuket.html", reply_markup=markup')
    elif message.text == 'Кафе' and place == "Чангмай":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Restaurant_Review-g293917-d25110134-Reviews-Bodhi_Terrace-Chiang_Mai.html')
    elif message.text == 'Кафе' and place == "Банкок":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Restaurant_Review-g293916-d27039273-Reviews-Babyccino_Co-Bangkok.html')
    elif message.text == 'Вернутся в главное меню':
        start_message(message)

    # ОТЕЛЬ
    elif message.text == 'Отель' and place == "Пхукет":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Hotel_Review-g10804710-d535970-Reviews-Beyond_Karon-Karon_Beach_Karon_Phuket.html')
    elif message.text == 'Отель' and place == "Чангмай":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Hotel_Review-g293917-d7620257-Reviews-Akyra_Manor_Chiang_Mai-Chiang_Mai.html')
    elif message.text == 'Отель' and place == "Банкок":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Hotel_Review-g293916-d13134217-Reviews-Akara_Hotel-Bangkok.html')
    elif message.text == 'Вернутся в главное меню':
        start_message(message)

    # BEACH
    if message.text == 'Beach' and place == "Phuket":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Attraction_Review-g1210687-d450974-Reviews-Kata_Beach-Kata_Beach_Karon_Phuket.html')
    elif message.text == 'Beach' and place == "Chiang Mai":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Hotel_Review-g293917-d17519162-Reviews-Riverside_Luxury_Pool_Villa_88_Place-Chiang_Mai.html')
    elif message.text == 'Beach' and place == "Bangkok":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Restaurant_Review-g293916-d27039273-Reviews-Babyccino_Co-Bangkok.html')
    elif message.text == 'Back to main menu':
        start_message(message)

    # CAFES
    elif message.text == 'Cafes' and place == "Phuket":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Restaurant_Review-g1215781-d25184563-Reviews-The_5th_Element_Phuket-Phuket_Town_Phuket.html", reply_markup=markup')
    elif message.text == 'Cafes' and place == "Chiang Mai":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Restaurant_Review-g293917-d25110134-Reviews-Bodhi_Terrace-Chiang_Mai.html')
    elif message.text == 'Cafes' and place == "Bangkok":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Restaurant_Review-g293916-d27039273-Reviews-Babyccino_Co-Bangkok.html')
    elif message.text == 'Back to main menu':
        start_message(message)
    # HOTEL
    elif message.text == 'Hotel' and place == "Phuket":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Hotel_Review-g10804710-d535970-Reviews-Beyond_Karon-Karon_Beach_Karon_Phuket.html')
    elif message.text == 'Hotel' and place == "Chiang Mai":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Hotel_Review-g293917-d7620257-Reviews-Akyra_Manor_Chiang_Mai-Chiang_Mai.html')
    elif message.text == 'Hotel' and place == "Bangkok":
        bot.send_message(message.chat.id,
                         text='https://www.tripadvisor.ru/Hotel_Review-g293916-d13134217-Reviews-Akara_Hotel-Bangkok.html')
    elif message.text == 'Back to main menu':
        start_message(message)


if __name__ == '__main__':
    bot.infinity_polling()
