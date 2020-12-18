# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__ (self, car_speed, car_color, car_name, police):
        self.speed = car_speed
        self.color = car_color
        self.name = car_name
        self.is_police = police

    def go (self):
        print (f'едет {self.name}')

    def stop (self):
        print (f'останавливается {self.name}')

    def turn (self, direction):
        print ('{} поворачивает {}'.format (self.name, direction))

    def show_speed (self):
        print (f'скорость {self.speed}')


class TownCar (Car):
    def show_speed (self):
        super ().show_speed ()
        if self.speed () > 60:
            print ('превышение скорости')


class SportCar (Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed() > 60:
            print('превышение скорости')


class PoliceCar (Car):
    pass


town_c = TownCar(100,'red','aaa',False)
sport_c = SportCar(100,'red','aaa',False)
work_c = WorkCar(100,'red','aaa',False)
police_c = PoliceCar(100,'red','aaa',True)

town_c.show_speed()
sport_c.show_speed()
work_c.show_speed()
police_c.show_speed()
