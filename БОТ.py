import vk_api 
import random 
from vk_api.longpoll import VkLongPoll, VkEventType 
import joke 
import coin 
from course import get_course
from wiki import get_summary
import meme
import news
import fact
import cities
import advice
 
 
def main():
 
    TOKEN = "4a17250a79cb1fbab5a2122f96be1dfecca9b60e4d5eba8b7f6228fff595b9be470a27b61d2522cb4eb5e"
 
    vk_session = vk_api.VkApi(token=TOKEN)
 
    vk = vk_session.get_api()
 
    longpoll = VkLongPoll(vk_session)
 
    bot_info = """ 
    Меня зовут Бот Печенька, я готов тебе помочь:
    напишешь мне "-с" (любой объект, город, страну) и я расскажу об этом
    напишешь мне "шутка" и я кину тебе шутку 
    напишешь мне "монетка" и я флипну монетку 
    напишешь мне "курс" и я расскажу про курс валют 
    напишешь мне "мем" и я кину тебе мемас
    напишешь мне "погода" (город) и я расскажу про погоду 
    напишешь мне "игра" и мы с тобой поиграем
    напишешь мне "новости" и я кину тебе новости всего мира
    напишешь мне "факт" и я расскажу тебе то, чего ты не знал
    напишешь мне "совет" и я помогу тебе с выбором
    """ 

    play_time = """
    если хочешь сыграть в города - "города"
    """

    
    advice_time = """
    напиши мне "сериал" и я порекомендую тебе сериал
    напиши мне "фильм" и я порекомендую тебе фильм
    напиши мне "книга" и я порекомендую тебе книгу
    """
 
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg_text = event.text.lower()
            query = msg_text[:2]
            text = msg_text[3:]
            message_id = random.randint(10, 999999999999)
 
            if msg_text == "инфа":
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=bot_info)

            elif query == "-с":
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=get_summary(text))

            elif msg_text == "шутка": 
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=joke.get_joke())

            elif msg_text == "монетка": 
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=coin.get_coin())

            elif msg_text == "погода": 
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=main(text))

            elif msg_text == "курс":
                responce = "{0} рублей за 1 доллар \n {1} рулей за 1 евро \n {2} рублей за 10 юаней \n {3} рублей за 1 фунт"
                responce = responce.format(get_course("R01235"), get_course("R01239"), get_course("R01375"), get_course("R01035"))
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=responce)

            elif msg_text == "новости":
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=news.format_news())

            elif msg_text == "мем":
                vk.messages.send(user_id=event.user_id, random_id=message_id, message="смешно?", attachment=meme.get_memes())

            elif msg_text == "факт":
                vk.messages.send(user_id=event.user_id, random_id=message_id, attachment=fact.get_facts())

            elif msg_text == "игра":
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=play_time)

            elif msg_text == "города":
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=cities.get_cities())

            elif msg_text == "совет":
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice_time)

            elif msg_text == "сериал":
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.get_series_genre())
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                        msg_text = event.text.lower()
                        text = msg_text[3:]
                        message_id = random.randint(10, 999999999999)
                        if msg_text == "фантастика":
                            vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.series_fantasy())
                        elif msg_text == "комедия":
                            vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.series_comedy())
                        elif msg_text == "боевик":
                            vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.series_thriller())
                        elif msg_text == "ужастик":
                            vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.series_horor())
                        elif msg_text == "драма":
                            vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.series_drama())

            elif msg_text == "фильм":
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.get_films_genre())
                if msg_text == "фантастика":
                    vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.films_fantasy())
                elif msg_text == "комедия":
                    vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.films_comedy())
                elif msg_text == "боевик":
                    vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.films_thriller())
                elif msg_text == "ужастик":
                    vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.films_horor())
                elif msg_text == "драма":
                    vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.films_drama())

            elif msg_text == "книга":
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.get_books_genre())
                if msg_text == "детектив":
                    vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.books_detective())
                elif msg_text == "фантастика":
                    vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.books_fantasy())
                elif msg_text == "научная литература":
                    vk.messages.send(user_id=event.user_id, random_id=message_id, message=advice.books_literature())

            else:
                vk.messages.send(user_id=event.user_id, random_id=message_id, message=bot_info)
 
main()
