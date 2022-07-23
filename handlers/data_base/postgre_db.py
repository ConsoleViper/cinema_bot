import psycopg
from botConfiguration import bot

async def sql_CreateTable():
    async with await psycopg.AsyncConnection.connect("dbname=cinema_bot user=postgres password=People211") as connect:
    
        async with connect.cursor() as cur:
            await cur.execute(
                """
                CREATE TABLE IF EXISTS going_films(
                    poster_img text,
                    film_title varchar(50) not null PRIMARY KEY,
                    genre varchar(50) not null,
                    age_limit smallint not null,
                    start_rental date,
                    finish_rental date,
                    description text not null,
                    film_url text;
                )
                """
            )
            await connect.commit()

async def sql_read(message):
    async with await psycopg.AsyncConnection.connect("dbname=cinema_bot user=postgres password=People211") as d_base:
        async with d_base.cursor() as cur:
            await cur.execute('SELECT * FROM going_films')
            #await cur.fetchall() смысла его испльзовать не было, так как fetchall возвращает список значений
            async for film in cur:
                await bot.send_photo(message.from_user.id, film[0], f"Нащва фільму: {film[1]}\nЖанр: {film[2]}\nВікове обмеження: {film[3]}+\nДата показу: з {film[4]} по {film[5]}\nКороткий опис: {film[6]}\n") # добавить inline кнопку
                
