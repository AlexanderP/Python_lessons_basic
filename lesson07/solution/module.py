import random


# строка карточки
class CardRow:
    __numbers = []

    @property
    def numbers(self):
        return self.__numbers

    @numbers.setter
    def numbers(self, numbers: list):
        if len(numbers) != 5:
            raise ValueError
        else:
            self.__numbers = []
            for x in numbers:
                self.__numbers.append(x)

            self.__numbers.sort()  # 0 -> 9

            while len(self.__numbers) < 9:
                random_index = random.randint(0, len(self.__numbers))
                self.__numbers.insert(random_index, '__')

    def check_number(self, value):
        if value in self.__numbers:
            index = self.__numbers.index(value)
            self.__numbers[index] = '--'

            return True
        else:
            return False

    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        num_list = list(map(str, self.numbers))
        num_list = [x.rjust(2) for x in num_list]
        result_str = "-".join(num_list)

        return result_str

    def __repr__(self):
        return self.__str__()


# карточка
class Card:
    __rows = []

    def __init__(self):
        random_numbers = random.sample(range(1, 90 + 1), k=15)
        self.rows = random_numbers

    def __str__(self):
        return self.rows

    def is_number_exists(self, number):
        for row in self.__rows:
            if number in row.numbers:
                return True
        else:
            return False

    def check_number(self, number):
        for row in self.__rows:
            if number in row.numbers:
                row.check_number(number)

    @property
    def rows(self):
        return "\n".join([str(row) for row in self.__rows])

    @rows.setter
    def rows(self, numbers):
        self.__rows = []

        number_step = 0
        for _ in range(3):
            self.__rows.append(CardRow(numbers[number_step:number_step + 5]))
            number_step += 5

    @property
    def is_completed(self):
        status = True

        for row in self.__rows:
            only_integer_values = list(filter(
                lambda x: isinstance(x, int),
                row.numbers
            ))

            if len(only_integer_values) > 0:
                status = False

        return status


# итератор бочонков
class BoxIterator:
    def __init__(self, count=90):
        self.boxes = [x for x in range(1, count + 1)]
        self.box_index = -1

        random.shuffle(self.boxes)

    def __iter__(self):
        return self

    def __next__(self):
        if self.box_index < len(self.boxes) - 1:
            self.box_index += 1
            print(f"Boxes remain: {len(self.boxes) - self.box_index}")

            return self.boxes[self.box_index]
        else:
            raise StopIteration


# игрок
class Player:
    def __init__(self, name: str, card: Card):
        self.name = name
        self.card = card

    def __str__(self):
        return f"{'_' * 20}\nPlayer: {self.name}\nCard: \n{self.card}"

    def __repr__(self):
        return f"\n{self.__str__()}\n"
