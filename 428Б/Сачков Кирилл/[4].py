import math

class Radar:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.latitude = 0  # Широта радара
            cls._instance.longitude = 0  # Долгота радара
            cls._instance.altitude = 0  # Высота радара
        return cls._instance


    def emit_pulse(self, azimuth, elevation):
        print(f"Радар излучил импульс. Азимут: {azimuth} градусов, Угол места: {elevation} градусов.")


class FlyingObject:
    def __init__(self, x, y, z, velocity_x, velocity_y, velocity_z):
        self.x = x
        self.y = y
        self.z = z
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.velocity_z = velocity_z

    # Метод для обновления позиции объекта
    def update_position(self, time):
        self.x += self.velocity_x * time
        self.y += self.velocity_y * time
        self.z += self.velocity_z * time

# Функция для конвертации декартовых координат в сферические
def cartesian_to_spherical(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    azimuth = math.degrees(math.atan2(y, x))
    elevation = math.degrees(math.asin(z / r))
    return r, azimuth, elevation


radar = Radar()


objects = [
    FlyingObject(100, 200, 50, 5, 10, 2),
    FlyingObject(-50, 150, 70, 8, -3, 5)
]

# Вывод текущих сферических координат объектов относительно радара
print("Текущие координаты объектов относительно радара:")
for obj in objects:
    r, azimuth, elevation = cartesian_to_spherical(obj.x, obj.y, obj.z)
    print(f"Расстояние: {r} м, Азимут: {azimuth} градусов, Угол места: {elevation} градусов.")

# Ввод времени с клавиатуры
time = float(input("Введите время в секундах: "))

# Обновление координат и вывод новых координат после времени time
print(f"Новые координаты объектов относительно радара после {time} секунд:")
for obj in objects:
    obj.update_position(time)
    r, azimuth, elevation = cartesian_to_spherical(obj.x, obj.y, obj.z)
    print(f"Расстояние: {r} м, Азимут: {azimuth} градусов, Угол места: {elevation} градусов.")