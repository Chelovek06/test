import random

genre = ['комедия',' боевик',' ужастик',' драма',' фантастика']
genre_book = ['детектив',' фантастика',' научная литература']

series_comedy = ['Друзья',' Теория большого взрыва',' Клиника']
series_drama = ['Ходячие мертвецы',' Агенты "Щ.И.Т."',' Игра престолов']
series_thriller = ['Ходячие мертвецы',' Бригада']
series_fantasy = ['Флэш',' Одарённые',' Чёрная материя']
series_horor = ['Призраки дома на холме',]


films_comedy = ['','','']
films_drama = ['','','']
films_thriller = ['Железный человек',' Железный человек 2',' Железный человек 3',' Первый мститель: Другая война',' Мстители: Эра Альтрона',
                  ' Доктор Стрэндж',' Первый мститель',' Мстители',' Веном']
films_fantasy = ['Тор',' Тор 2: Царство тьмы',' Первый мститель: Другая война',' Стражи Галактики',' Мстители: Эра Альтрона',' Человек_муравей',
                 ' Первый мститель: Противостояние',' Доктор Стрэндж',' Стражи Галактики 2',' Человек-паук: Возврашение домой',' Тор: Рагнарёк',
                 ' Чёрная Пантера',' Мстители: Война бесконечности',' Человек-муравей и Оса',' Веном',' Мстители',' Первый мститель']
films_horor = ['Астрал',' Астрал 2',' Астрал 3',' Астрал 4: Последний ключ'] 

books_detective = ['Рассказы о Шерлоке Холмсе',' Лунный камень',' Брокер']
books_fantasy = ['Обречённые на победу',' Ложная слепота',' Алгебраист']
books_literature = ['Тайная мать',' Алая лента',' День цезарей']

def get_series_genre():
    return(genre)

def get_films_genre():
    return(genre)

def get_books_genre():
    return(genre_book)

def get_films():
    def films_fantasy():
        return random.choice(films_fantasy)
    def films_thriller():
        return random.choice(films_thriller)
    def films_drama():
        return random.choice(films_drama)
    def films_comedy():
        return random.choice(films_comedy)
    def films_horor():
        return random.choice(films_horor)
    
def get_series():
    def series_fantasy():
        return random.choice(series_fantasy)
    def series_thriller():
        return random.choice(series_thriller)
    def series_drama():
        return random.choice(series_drama)
    def series_comedy():
        return random.choice(series_comedy)
    def series_horor():
        return random.choice(series_horor)
    
def get_books():
    def books_detective():
        return random.choice(books_detective)
    def books_fantasy():
        return random.choice(books_fantasy)
    def books_literature():
        return random.choice(books_literature)
