class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} поехал'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} повернул на право'

    def turn_left(self):
        return f'{self.name} повернул на лево'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше, чем положена городскому автомобилю'
        else:
            return f'Скорость {self.name} в норме для городского автомобиля'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'выше, чем положена рабочему автомобилю.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} это полицейский автомобиль'
        else:
            return f'{self.name} это не полицейский автомобиль'


Volkswagen = SportCar(100, 'Brown', 'Volkswagen', False)
Oka = TownCar(30, 'White', 'Oka', False)
Lada = WorkCar(70, 'Black', 'Lada', True)
Ford = PoliceCar(110, 'Blue',  'Ford', True)
print(Lada.turn_left())
print(f'{Oka.turn_right()}, {Volkswagen.stop()}.')
print(f'{Lada.go()} со скоростью {Lada.show_speed()}')
print(f'Цвет {Lada.name} - {Lada.color}.')
print(f'{Volkswagen.name} полицейский автомобиль? {Volkswagen.is_police}')
print(f'{Lada.name} полицейский автомобиль? {Lada.is_police}')
print(Volkswagen.show_speed())
print(Oka.show_speed())
print(Ford.police())
print(Ford.show_speed())