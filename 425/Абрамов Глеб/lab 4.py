import math

# Определение класса для представления трехмерных векторов
class Vector3D:
    def __init__(self, x, y, z):
        # Инициализация компонентов вектора
        self.x = x
        self.y = y
        self.z = z

    # Метод для сложения двух векторов
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    # Метод для вычитания одного вектора из другого
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    # Метод для умножения вектора на скаляр
    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    # Метод для вычисления расстояния до другого вектора
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z) ** 2)

    # Метод для преобразования декартовых координат в сферические
    def to_spherical(self):
        r = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        theta = math.atan2(math.sqrt(self.x**2 + self.y**2), self.z)  # угол места
        phi = math.atan2(self.y, self.x)  # азимут
        return r, math.degrees(theta), math.degrees(phi)

# Реализация паттерна Singleton для класса Radar
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# Класс радара, использующий паттерн Singleton
class Radar(metaclass=SingletonMeta):
    def __init__(self, position):
        self.position = position

    # Метод для получения сферических координат объекта
    def get_object_coordinates(self, flying_object):
        relative_position = flying_object.position - self.position
        return relative_position.to_spherical()

    # Метод для предсказания сферических координат объекта через время t
    def predict_object_coordinates(self, flying_object, time):
        future_position = flying_object.position + flying_object.velocity * time
        relative_position = future_position - self.position
        return relative_position.to_spherical()

# Класс для представления летающих объектов
class FlyingObject:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

# Главная функция программы
def main():
    radar_position = Vector3D(0, 0, 0)  # координаты радара
    radar = Radar(radar_position)

    num_objects = int(input("Введите количество летающих объектов: "))
    flying_objects = []

    for i in range(num_objects):
        x, y, z = map(float, input(f"Введите координаты объекта {i + 1} (x y z): ").split())
        vx, vy, vz = map(float, input(f"Введите скорость объекта {i + 1} (vx vy vz): ").split())
        flying_objects.append(FlyingObject(Vector3D(x, y, z), Vector3D(vx, vy, vz)))

    print("\nТекущие сферические координаты объектов относительно радара:")
    for i, obj in enumerate(flying_objects):
        r, theta, phi = radar.get_object_coordinates(obj)
        print(f"Объект {i + 1}: r={r:.2f} м, θ(угол)={theta:.2f}°, φ(азимут)={phi:.2f}°")

    time = float(input("\nВведите время в секундах: "))
    print("\nСферические координаты объектов относительно радара через это время:")
    for i, obj in enumerate(flying_objects):
        r, theta, phi = radar.predict_object_coordinates(obj, time)
        print(f"Объект {i + 1}: r={r:.2f} м, θ(угол)={theta:.2f}°, φ(азимут)={phi:.2f}°")


if __name__ == "__main__":
    main()