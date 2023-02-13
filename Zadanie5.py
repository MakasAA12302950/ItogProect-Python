"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

ARGS = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
print(YA_PING.stdout)
for line in YA_PING.stdout:
    result = chardet.detect(line)
    print(line.decode(result['encoding']))
    
#с установкой модуля charted возникли проблемы. 
#Честно признаюсь переписала решение с вашего показа на семинаре, проверить его работу не могу. 
#Как будет время вернусь к этому заданию 
