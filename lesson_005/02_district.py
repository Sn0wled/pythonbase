# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код

import district

folks = []
folks.extend(district.soviet_street.house1.room1.folks)
folks.extend(district.soviet_street.house1.room2.folks)
folks.extend(district.soviet_street.house2.room1.folks)
folks.extend(district.soviet_street.house2.room2.folks)
folks.extend(district.central_street.house1.room1.folks)
folks.extend(district.central_street.house1.room2.folks)
folks.extend(district.central_street.house2.room1.folks)
folks.extend(district.central_street.house2.room2.folks)

print('На районе живут', ', '.join(folks))
