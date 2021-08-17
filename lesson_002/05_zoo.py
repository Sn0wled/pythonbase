#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

animals = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
animals.insert(1, 'bear')
print(animals)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
animals.extend(birds)
print(animals)

# уберите слона
#  и выведите список на консоль
del animals[animals.index('elephant')]
print(animals)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
print('Лев сидит в клетке номер ', animals.index('lion') + 1, ', а жаворонок в клетке номер ', animals.index('lark') + 1)


