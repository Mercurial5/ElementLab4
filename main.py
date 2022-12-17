from dataclasses import dataclass


@dataclass
class Person:
    fullname: str
    age: int

    def __str__(self):
        return f'Имя: {self.fullname}\nВозраст: {self.age}'


@dataclass
class Engine:
    power: int
    company: str

    def __str__(self):
        return f'Мощность: {self.power}\nПроизводитель: {self.company}'


@dataclass
class Driver(Person):
    experience: str

    def __str__(self):
        return f'{super().__str__()}\nСтаж: {self.experience}'


@dataclass
class Car:
    model: str
    type: str
    weight: int
    driver: Driver
    engine: Engine

    def start(self):
        print('Поехали')

    def stop(self):
        print('Останавливаемся')

    def turnRight(self):
        print('Поворот направо')

    def turnLeft(self):
        print('Поворот налево')

    def __str__(self):
        return f'Модель: {self.model}\nКласс: {self.type}\nВес: {self.weight}\nВодитель: {self.driver}' \
               f'\nМотор: {self.engine} '


@dataclass
class Lorry(Car):
    carrying: int

    def __str__(self):
        return f'{super().__str__()}\nГрузоподъёмность: {self.carrying}'


@dataclass
class SportCar(Car):
    speed: float

    def __str__(self):
        return f'{super().__str__()}\nСкорость: {self.speed}'
