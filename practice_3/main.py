# 1 задание
g = (x * 3 for x in [1,2,3])
a = list(g)
print(a)

# 2 задание
def announce(func):
    def wrapper():
        print("Внимание")
        result = func()
        print("Готово")
        return result
    return wrapper

@announce
def hello():
    print("Привет!")

hello()
