#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами
from pprint import  pprint

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'печенье':[
        {'shop': 'ашан', 'price': shops['ашан'][0]['price']},
        {'shop': 'пятерочка', 'price': shops['пятерочка'][0]['price']},
        {'shop': 'магнит', 'price': shops['магнит'][0]['price']}
    ],
    'конфеты':[
        {'shop': 'ашан', 'price': shops['ашан'][1]['price']},
        {'shop': 'пятерочка', 'price': shops['пятерочка'][1]['price']},
        {'shop': 'магнит', 'price': shops['магнит'][1]['price']}
    ],
    'карамель':[
        {'shop': 'ашан', 'price': shops['ашан'][2]['price']},
        {'shop': 'пятерочка', 'price': shops['пятерочка'][2]['price']},
        {'shop': 'магнит', 'price': shops['магнит'][2]['price']}
    ],
    'пирожное':[
        {'shop': 'ашан', 'price': shops['ашан'][3]['price']},
        {'shop': 'пятерочка', 'price': shops['пятерочка'][3]['price']},
        {'shop': 'магнит', 'price': shops['магнит'][3]['price']}
    ]
}

pprint(sweets)
# Указать надо только по 2 магазина с минимальными ценами

