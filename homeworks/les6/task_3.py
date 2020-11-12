class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

first = Position('Иван', 'Петров', 'инженер', 100000, 25000)
print(f'Полное имя: {first.get_full_name()}')
print(f'Должность: {first.position}')
print(f'Доход: {first.get_total_income()}\n')

second = Position('Василий', 'Иванов', 'рабочий', 30000, 5000)
print(f'Полное имя: {second.get_full_name()}')
print(f'Должность: {second.position}')
print(f'Доход: {second.get_total_income()}')