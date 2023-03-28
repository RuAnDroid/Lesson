# import sqlite3 as sq

# con = sq.connect('profile.db')  # db,db3,sqlite,sqlite3
# cur = con.cursor()
#
# cur.execute("""""")
#
# con.close()
# with sq.connect('profile.db') as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # data BLOB
#     # )""")
#     cur.execute("DROP TABLE users")

# with sq.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     DROP TABLE person
#     """)
    # cur.execute("""CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT '+79090000000',
    # age INTEGER NOT NULL CHECK(age>15 AND age<70),
    # email TEXT UNIQUE
    # )""")

# with sq.connect('db_3.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM T1
#     ORDER BY FNAME
#     LIMIT 2, 5
#     """)
#
#
#     res = cur.fetchone()
#     # res2 = cur.fetchmany()
#     res1 = cur.fetchall()
#     print(res)
#     print(res1)
#     # for res in cur:
#     #     print(res)
#


# import sqlite3 as sq


# cars = [
#     ('BMW', 54000),
#     ('Chevrolet',56000),
#     ('Daewoo',38000),
#     ('Citroen',29000),
#     ('Honda',33000)
# ]
#
# with sq.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100
#     """)
    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

    # cur.executemany("INSERT INTO cars VALUES(NULL,?,?)", cars)

    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL,?,?)", car)

    # cur.execute("INSERT INTO cars VALUES(1,'Renault',20000)")
    # cur.execute("INSERT INTO cars VALUES(2,'Volvo',29000)")
    # cur.execute("INSERT INTO cars VALUES(3,'Mercedes',57000)")
    # cur.execute("INSERT INTO cars VALUES(4,'Bentley',35000)")
    # cur.execute("INSERT INTO cars VALUES(5,'Audi',52000)")
# con.commit()
# con.close()

# con = None
# try:
#     con =sq.connect('cars.db')
#     cur= con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL,'Renault',20000);
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print(f"Ошибка выполнения запроса {e}")
# finally:
#     if con:
#         con.close()

# with sq.connect('cars.db') as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
#
#     cur.execute("SELECT model, price FROM cars")
#     # rows =cur.fetchall()
#     # rows =cur.fetchone()
#     # rows = cur.fetchmany(5)
#     # print(rows)
#     for res in cur:
#         print(res['model'], res['price'])

# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
# with sq.connect('cars.db') as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         ava BLOB
#     );
#     """)
#     img = read_ava(1)
#     if img:
#         binary = sq.Binary(img)
#         cur.execute(("INSERT INTO users VALUES (?, ?)"),(1, binary))
#
# with sq.connect('cars.db') as con:
#     cur = con.cursor()
#
#
#     # with open("sql_dump.sql", "w") as f:
#     #     for sql in con.iterdump():
#     #         f.write(sql)
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)


# from jinja2 import Template

# name = "Игорь"
# age = 28
# per = {'name': 'Игорь', 'age': 28}

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
# per = Person("Игорь" , 26)
# tm = Template("Мне {{p.get_age()}} лет. Меня зовут {{p.get_name().upper() }}.")
# msg = tm.render(p=per)


# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Ярославль'},
#     {'id': 5, 'city': 'Уфа'}
# ]
#
# link = """<select name="cities">
# {% for c in cities -%}
# {%if c.id > 3 -%}
#     <option value="{{c.id}}>{{c['city']}}</option>
# {% elif c.city =='Москва' -%}
#     <option>{{c.city}}</option>
# {% else -%}
#     {{ c.city }}
#
# {% endif -%}
# {% endfor -%}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

# menu = [{'id': 'index', 'title': 'Главная'},
#         {'id': 'news', 'title': 'Новости'},
#         {'id': 'about', 'title': 'О компании'},
#         {'id': 'shop', 'title': 'Магазин'},
#         {'id': 'contacts', 'title': 'Контакты'},
#         ]
# link = """<ul>{%for i in menu -%}
# {%if i.title=='Главная'-%}
#     <li><a href="/{{i.id}}" class="active">{{i.title}}</a></li>
# {%else-%}
#     <li><a href="/{{i.id}}">{{i.title}}</a></li>
# {%endif-%}
# {%endfor-%}
# </ul>"""
# tm = Template(link)
# msg = tm.render(menu=menu)
# print(msg)

# cars = [{'model': 'Audi', 'price': 23000},
#         {'model': 'Skoda', 'price': 17300},
#         {'model': 'Renault', 'price': 44300},
#         {'model': 'Wolksvagen', 'price': 21300}
#         ]
# print(sum(map(lambda x: x['price'],cars)))
# sum1 = 0
# for i in cars:
#         sum1 += i['price']
# print(sum1)
# tp1 = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
# tm = Template(tp1)
# msg = tm.render(cs=cars)
# print(msg)

# html = """
# {% macro input(name, value='', type='text', size= 20) %}
#         <input type='{{type}}' name='{{name}}' value='{{value}}' size='{{size}}'>
# {% endmacro %}
#
# <p>{{ input('username', 'ann')}}</p>
# <p>{{ input('email')}}</p>
# <p>{{ input('password',type='password')}}</p>
# """
# tm = Template(html)
# msg = tm.render()
# print(msg)

# html = """
# {% macro input(name, type='text', placeholder='') -%}
#     <input type='{{ type }}' name='{{ name }}' placeholder='{{ placeholder }}'>
# {%- endmacro %}
# <p>{{ input('firstname', placeholder="Имя") }}</p>
# <p>{{ input('lastname', placeholder="Фамилия") }}</p>
# <p>{{ input('address', placeholder="Адрес") }}</p>
# <p>{{ input('phone', type='tel', placeholder="Телефон") }}</p>
# <p>{{ input('email', type='email', placeholder="Почта") }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)

# persons = [{"name": "Алексей", "year": 18, "weight": 78.5},
#            {"name": "Никита", "year": 28, "weight": 82.3},
#            {"name": "Виталий", "year": 33, "weight": 94.0}]
#
# html = """
# {% macro list_users(list_of_users)%}
# <ul>
# {% for u in list_of_users -%}
#     <li>{{u.name}} {{caller(u) }}</li>
# {% endfor -%}}
# </ul>
# {% endmacro %}
#
# {% call(user) list_users(users) %}
#     <ul>
#     <li>{{ user.year }}</li>
#     <li>{{ user.weight }}</li>
#     </ul>
# {% endcall %}
# """
#
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)

# from jinja2 import Environment, FileSystemLoader

# persons = [{"name": "Алексей", "year": 18, "weight": 78.5},
#            {"name": "Никита", "year": 28, "weight": 82.3},
#            {"name": "Виталий", "year": 33, "weight": 94.0}
#            ]

# subs =['Культура','Наука ','Политика','Спорт']
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
#
# # tm = env.get_template('main.html')
# # msg = tm.render(users=persons, title='About Jinja')
#
# tm = env.get_template('about.html')
# msg = tm.render(list_table=subs)
# print(msg)
