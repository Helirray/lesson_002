#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

first_movie = my_favorite_movies[0:10]
last_movie = my_favorite_movies[-15:-1] + my_favorite_movies[-1]
second_movie = my_favorite_movies[12:25]
second_from_last_movie = my_favorite_movies[-22:-17]
print(first_movie, last_movie, second_movie, second_from_last_movie)
