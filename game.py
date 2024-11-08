from typing import Self
from random import choice
from winsound import Beep
from abc import ABC, abstractmethod
from enum import Enum


class WeaponPower(Enum):
    SHIP = 20
    PLANE = 30
    DRONE = 12


print(WeaponPower.SHIP)
print(WeaponPower.SHIP.value)
print(WeaponPower.SHIP.name)


class BaseLifePoints(Enum):
    BASE = 100
    DRONE = 1


class Constants:
    SHIP_WEAPON_POWER = 20
    PLANE_WEAPON_POWER = 30
    DRONE_WEAPON_POWER = 12
    LIFE_POINTS = 100
    LIFE_POINTS_DRONE = 1


class GameCharacter(ABC):
    def __init__(self, name, payload, life_points, weapon_power):
        self.name = name
        self.payload: int = payload
        self.__life_points = life_points
        self._weapon_power = weapon_power

    @property
    def life_points(self):
        return self.__life_points

    @life_points.setter
    def life_points(self, value):
        print(1111111111111111111111111111111111111111111111)
        self.__life_points = value

    @property
    def is_alive(self):
        return self.__life_points > 0

    def __str__(self):
        return f'{self.name} - is_alive={self.is_alive}, payload={self.payload}, health={self.__life_points}'

    def attack(self, other: Self = None):
        if not self.is_alive:
            print(self, 'is died already')
            return

        if not self.payload:
            print('no payload', self)
            return

        self.payload -= 1
        if not other:
            print('just for fun')
            return

        is_enemy_hit = choice([True, False])
        if is_enemy_hit:
            other.__life_points -= self._weapon_power
            print(other, 'was hit')

    @abstractmethod
    def make_noize(self):
        pass


class Ship(GameCharacter):
    def __init__(self, name, payload):
        super().__init__(name, payload, Constants.LIFE_POINTS, WeaponPower.SHIP.value)

    def make_noize(self):
        Beep(5000, 1)


class Plane(GameCharacter):
    def __init__(self, name, payload):
        super().__init__(name, payload, Constants.LIFE_POINTS, Constants.PLANE_WEAPON_POWER)
        self.wings = 2

    def make_noize(self):
        Beep(10000, 1)


class Drone(GameCharacter):
    def __init__(self, name, payload):
        super().__init__(name, payload, Constants.LIFE_POINTS_DRONE, Constants.DRONE_WEAPON_POWER)
        self.payload = 1

    def attack(self, other: GameCharacter = None):
        print(self, 'is attacking')
        super().attack(other=other)
        self.life_points = 0

    def make_afraid(self, other: GameCharacter = None):
        print(self, 'is attacking')
        self.life_points = 0

    def make_noize(self):
        Beep(32000, 10)


# strange = GameCharacter(2222, 555, 555, 666)


plane = Ship('Assol', 20)
plane2 = Plane('Assol2', 20)
drone = Drone('mavic', 1)

plane.attack(plane2)
plane.attack(plane2)
plane.attack(plane2)
plane.attack(plane2)
plane2.attack(plane)
plane2.attack(plane)
plane2.attack(plane)

plane.attack(plane)
plane.attack()
plane.attack()

drone.attack(plane)
drone.attack(plane)
drone.attack(plane)
drone.attack(plane)
drone.attack(plane)
drone.make_noize()

pass
