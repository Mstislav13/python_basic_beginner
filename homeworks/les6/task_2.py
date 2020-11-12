class Road:
    __length = None
    __width = None
    weigth = None
    thickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def intake(self):
        self.weigth = 25
        self.thickness = 0.05
        intake = self.length * self.width * self.weigth * self.thickness / 1000
        print(f'Для создания дорожного покрытия нужно {intake} тонн асфальта.')

road_to_village = Road(20000, 6)
road_to_village.intake()
