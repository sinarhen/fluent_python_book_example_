colors = 'black white red'
sizes = 'XS S M L XL'
lst = [f'Футболка цвета:{color}, Размера {size}' for size in sizes.split() for color in colors.split()]
print(lst)
shirt = [f'Футболка цвета {color}, размера {size}' for size in sizes.split() for color in colors.split()]
