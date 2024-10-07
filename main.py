from telebot import TeleBot, types
from telebot.util import quick_markup

import tomllib

from create_strings import email_list, subject_dict

with open(".secret.toml", "rb") as f:
    data = tomllib.load(f)
    ALLOWED_ID = data['secret']['allowed_id']
    token = data['secret']['token']

main_dict = {
        'Emails' : {'callback_data': 'emails' },
        'Subjects' : {'callback_data': 'subjects'},
        'Credits' :{ 'callback_data': 'credits'}
    }

bot = TeleBot(token=token)

def check_id(func):
    def inner(message):
        if message.chat.id not in ALLOWED_ID:
            return
        return func(message)
    return inner

@bot.message_handler(commands = ['request_access'])
def request_access(message):
    print(message.chat.id)

@bot.message_handler(commands= ['start'])
@check_id
def test(message):
    bot.send_message(message.from_user.id, "Working now")

@bot.message_handler(commands=['schedule'])
@check_id
def main_menu(message):
    markup = quick_markup(main_dict, row_width=1)
    bot.send_message(message.from_user.id, text='Выберете дейcтвие', reply_markup=markup)

@bot.callback_query_handler(func=lambda message:True)
def submenus(message):
    if message.data == 'emails':
        markup = quick_markup({
            'Back' : {'callback_data': 'back_main' },
        }, row_width=1)        
        bot.edit_message_text(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
            text=email_list(),
            reply_markup=markup,
            parse_mode='MarkdownV2')
    elif message.data == 'subjects':
        markup = quick_markup(
            dict(subject_dict(),**{'Back' : {'callback_data': 'back_main' }, }),
            row_width=1)
        bot.edit_message_text(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
            text='subjects list',
            reply_markup=markup)
    elif message.data == 'credits':
        markup = quick_markup({
            'Back' : {'callback_data': 'back_main' },
        }, row_width=1)
        bot.edit_message_text(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
            text="any bugs report here:\n`onesecondch@gmail.com`",
            parse_mode='MarkdownV2',
            reply_markup=markup
            )
    elif message.data == 'back_main':
        markup = quick_markup(main_dict, row_width=1)
        bot.edit_message_text(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
            text='Выберете дейcтвие',
            reply_markup=markup
            )        

if __name__ == '__main__':
    bot.polling(non_stop=True, interval=0)