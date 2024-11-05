class Constants:
    SHIP_WEAPON_POWER = 2
    PLANE_WEAPON_POWER = 30
    DRONE_WEAPON_POWER = 12
    LIFE_POINTS = 100
    LIFE_POINTS_DRONE = 1


class GameCharacter:
    def __init__(self, name, payload, life_points, weapon_power):
        self.name = name
        self.payload = payload
        self.__life_points = life_points
        self._weapon_power = weapon_power

    @property
    def life_points(self):
        return self.__life_points

    @property
    def is_alive(self):
        return self.__life_points > 0

    def __str__(self):
        return self.name


class Ship(GameCharacter):
    def __init__(self, name, payload):
        super().__init__(name, payload, Constants.LIFE_POINTS, Constants.SHIP_WEAPON_POWER)


class Plane(GameCharacter):
    def __init__(self, name, payload):
        super().__init__(name, payload, Constants.LIFE_POINTS, Constants.PLANE_WEAPON_POWER)
        self.other = 55555


class Drone(GameCharacter):
    def __init__(self, name, payload):
        super().__init__(name, payload, Constants.LIFE_POINTS_DRONE, Constants.DRONE_WEAPON_POWER)


plane = Plane('Assol', 20)

pass
