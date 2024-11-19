#1 Условные операторы:

score = int(input("Введите вашы баллы: "))

if score >= 90:
    print("Отлично")
elif score >= 70:
    print("Хорошо")
elif score >= 60:
    print("Удовлетворительно")
elif score <= 59:
    print("Неудовлетворительно")
else:
    print("Ошибка данных")


#2 Списки и кортежи:

poem = ['Зимнее утро (Мороз и солнце; день чудесный)', 'Зимняя дорога', 'Туча', 'Уж небо осенью дышало', 'Осеннее утро']
print(poem)

user = input('Добавить стих - a, Удалить стих - b, Заменить стих - c, Удалить все стихи - d: ')

if user == 'a':
     add_poem = input('Введите стих, чтобы добавить: ')
     poem.append(add_poem)
     print(poem)
elif user == 'b':
     delete_poem = input('Введите стих, чтобы удалить: ')
     poem.remove(delete_poem)
     print(poem)
elif user == 'c':
     delete_poem = input('Введите стих, который хотите заменить: ')
     poem.remove(delete_poem)
     add_poem = input('Введите стих, чтобы добавить: ')
     poem.append(add_poem)
     print(poem)
elif user == 'd':
     poem.clear()
     print(poem)
else:
     print('Неизвестная операция')


#3 Циклы:

# for
books = ['Евгений Онегин', 'Мастер и Маргарита', 'Мертвые души', 'Война и мир']
for i in books:
    print(i)

# while
while True:
    c = input("Введите команду: ")
    if c == "q":
        break
    print(f"Вы ввели: {c}")


#4 List comprehension:

even_numbers = [num for num in range(1, 20) if num % 2 == 0]

print(even_numbers)


#5 Словари и сеты:

writing = {'Автор:': 'Михаил Булгаков', 'Произведение:': 'Мастер и Маргарита', 'Дата написания:': '1928—1940'}

for k, v in writing.items():
    print(k, v)


#6 Функции:

def a(x, y, z):
    return x + y + z

result = a(1, 2, 3)
print(result)


#7 Анонимные функции:

a = int(input('Введите число, чтобы проверить чётность: '))
even = lambda num: num % 2 == 0

print(even(a))


#8 Классы:

class Users:
    user_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Users.user_count += 1

    def display_count(self):
        print(f"Всего пользователей: {Users.user_count}")

    def display_user(self):
        print('Имя: {}. Возраст: {}'.format(self.name, self.age))

user1 = Users('Anya', 20)
user2 = Users('Misha', 21)
user3 = Users('Sasha', 19)

user1.display_count()
user1.display_user()
user2.display_user()
user3.display_user()


#9 Наследование:

class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name} ")

class Student(Person):
    def study(self):
        print(f"{self.name} - студент")

pavel = Student("Павел")
pavel.display_info()
pavel.study()