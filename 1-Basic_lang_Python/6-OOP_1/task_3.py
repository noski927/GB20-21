# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self):
        self.name = 'Mike'
        self.surname = 'Wazowski'
        self.position = 'Fish'
        self._income = {'wage': 5000, 'bonus': 1000 }


class Position(Worker):
    # def __init__(self):


    def get_full_name(self):
        print(f'{self.name} {self.surname} – {self.position} ')

    def get_total_income(self):
        print(self._income['wage']+self._income['bonus'])


plankton = Position()
plankton.get_full_name()
plankton.get_total_income()

