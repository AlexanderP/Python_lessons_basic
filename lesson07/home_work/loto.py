#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random
from time import sleep


class Cards(object):

    def __init__(self, player=False):
        self.cards_len = 9
        self.cards_str = 3
        self.cards_num = 5
        self.player = player
        self.count = 0
        self.count_max = self.cards_str * self.cards_num
        rand_lst = list(range(1, 91))
        random.shuffle(rand_lst)
        self.cards = [[] for _ in range(self.cards_str)]
        index = 0
        index_str = 0
        for _str in range(self.cards_str):
            self.cards[index_str] = ["  " for _ in range(self.cards_len)]
            list_index = sorted(random.sample(range(self.cards_len),
                                              self.cards_num))
            list_numbers = sorted(rand_lst[index:index + self.cards_num])
            index_number = 0
            for _index in list_index:
                if list_numbers[index_number] < 10:
                    self.cards[index_str][_index] = ' ' + str(
                        list_numbers[index_number])
                else:
                    self.cards[index_str][_index] = str(
                        list_numbers[index_number])

                index_number += 1
            index += self.cards_num
            index_str += 1

    def __str__(self):
        if self.player:
            name = 'Ваша карточка'
        else:
            name = 'Карточка компьютера'
        number_l = int(0.5 * (self.cards_len * 3 - len(name)))
        number_r = self.cards_len * 3 + 1 - len(name) - number_l
        text = number_l * '-' + name + number_r * '-' + '\n'
        for _index in range(self.cards_str):
            text += '|' + ' '.join(self.cards[_index]) + '|\n'
        text += (self.cards_len * 3 + 1) * '-'
        return text

    def find_number(self, number):
        string = str(number)
        if int(string) < 10:
            string = ' ' + string
        for _index in range(self.cards_str):
            if self.cards[_index].count(string):
                index_number = self.cards[_index].index(string)
                self.cards[_index][index_number] = " -"
                self.count += 1
                return True


class Sack(object):

    def __init__(self):
        self.numbers_list = list(range(1, 91))
        random.shuffle(self.numbers_list)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.numbers_list) > 0:
            return self.numbers_list.pop()
        else:
            raise StopIteration

    def __len__(self):
        return len(self.numbers_list)


class Lotto(object):

    def __init__(self):
        self.pc = Cards()
        self.player = Cards(True)
        self.sack = Sack()

    def start_game(self):
        print("Вас преведствует игра в лото!")
        for _number in self.sack:
            print("Вы опускаете руку в мешочек!")
            sleep(1)
            print(f"Достаете бочонок: {_number} (осталось {len(self.sack)})\n")
            print(self.player)
            print(self.pc)
            answer = input('Зачеркнуть цифру? (y/n) ')
            if answer.lower() == 'y':
                answer = True
            else:
                answer = False
            find_number_player = self.player.find_number(_number)
            self.pc.find_number(_number)
            if (find_number_player and not answer) or (not find_number_player
                                                       and answer):
                print('Вы проиграли!')
                break
            if self.player.count == self.player.count_max:
                print('Вы выйграли!')
                break
            if self.pc.count == self.pc.count_max:
                print('Выйграл компьютер!')
                break


lotto = Lotto()
lotto.start_game()
