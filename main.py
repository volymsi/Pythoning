# объявление функции
def draw_triangle():
    for i in range(8):
        print((7-i)*' ' + '*' * (i+1) + '*'*i)

# основная программа
draw_triangle()  # вызов функции