# Вариант 12

# Задание 1. Область видимости
x = 22

def show():
    x = 12
    print(x)

show()
print(x)


# Задание 2. Args
def total(*args):
    return sum(args)

print(total(12, 13, 14))


# Задание 3. Kwargs
def person(**kwargs):
    name = kwargs.get("name", "Гость")
    age = kwargs.get("age", 0)
    return name, age

print(person(name="Роман", age=18))


# Задание 4. Функция как параметр
def increase(x):
    return x + 2

def apply(func, value):
    return func(value)

print(apply(increase, 5))


# Задание 5. Рекурсия
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)
