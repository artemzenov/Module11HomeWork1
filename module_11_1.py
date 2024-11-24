import requests
import numpy
from PIL import Image


#Работа с библиотекой requests
params = {'q': 'Built-in Functions'}
req = requests.get('https://docs.python.org/3/search.html', params=params)
print(req.url, req.status_code)
print(req.text)

#Работа с библиотекой numpy
print()
array1 = numpy.array([[3, 6, 0], [2, 5, 4]])
print(f'массив данных:\n{array1}')
print(f'сумма элементов массива:\n{array1.sum()}')
print(f'максимальное значение в массиве:\n{array1.max()}')
print(f'минимальное значение в массиве:\n{array1.min()}')
print(f'массив, значение элементов которого увеличены в 2 раза:\n{array1 * 2}')
print(f'отсортированный массив:\n{numpy.sort(array1)}')

#Работа с библиотекой pillow
print()
with Image.open('images.jpeg') as foto:
    new_width, new_height = foto.width * 2, foto.height * 2
    foto = foto.resize((new_width, new_height))
    foto = foto.convert('L')
    foto.save('images_1.jpeg')