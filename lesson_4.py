# def mult(a, b):
#     result = a * b
#     return result
#
# def get_number(prompt):
#     while True:
#         try:
#             return int(input(prompt))  # или float, если нужны дробные
#         except ValueError:
#             print("Ошибка: нужно ввести целое число.")
#
# a = get_number('Введите первое число: ')
# b = get_number('Введите второе число: ')
#
# result = mult(a, b)
# print(result)

def func(a, b, *args, default=10, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"default={default}")
    print(f"kwargs={kwargs}")

func(1, 2, 3, 4, x=100, y=200)
# a=1, b=2
# args=(3, 4)
# default=10
# kwargs={'x': 100, 'y': 200}

friends = ['max', 'john', 'mark', 'juan' ]
result = []

for friend in friends:
    result.append(friend.upper())

result = list(map(str.lower, result))

def t(x):
    return x.title()
print(sorted(list(map(t, friends)),reverse=True))

fruits = ['apple', 'banana', 'orange', 'mango' ]
fruits_title = [x.title() for x in reversed(fruits)]
print(fruits_title)

#print(sorted(map(t, friends),reverse=True))