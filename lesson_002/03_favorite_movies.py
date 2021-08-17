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
print(my_favorite_movies[:my_favorite_movies.find(',')])
print(my_favorite_movies[my_favorite_movies.rfind(',') + 2:])
index_start = my_favorite_movies.find(',') + 2
index_end = my_favorite_movies.find(',', index_start)
print(my_favorite_movies[index_start:index_end])
index_end = my_favorite_movies.rfind(',')
index_start = my_favorite_movies.rfind(',', 0, index_end) + 2
print(my_favorite_movies[index_start:index_end])
