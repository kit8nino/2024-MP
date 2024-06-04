import math

# Класс Radar реализует паттерн Singleton, чтобы существовал только один экземпляр радара
class Radar:
    _instance = None

    def __new__(cls, x=0, y=0, z=0):
        if cls._instance is None:
            # Создание нового экземпляра радара и установка его координат
            cls._instance = super(Radar, cls).__new__(cls)
            cls._instance.x = x
            cls._instance.y = y
            cls._instance.z = z
        return cls._instance

    def get_position(self):
        # Возвращает декартовы координаты радара
        return (self.x, self.y, self.z)

    def to_spherical(self, x, y, z):
        # Преобразует декартовы координаты в сферические (радиус, азимут, угол места)
        dx = x - self.x
        dy = y - self.y
        dz = z - self.z
        r = math.sqrt(dx**2 + dy**2 + dz**2)  # Радиус
        azimuth = math.degrees(math.atan2(dy, dx))  # Азимут в градусах
        elevation = math.degrees(math.atan2(dz, math.sqrt(dx**2 + dy**2)))  # Угол места в градусах
        return (r, azimuth, elevation)

# Класс FlyingObject описывает летающий объект
class FlyingObject:
    def __init__(self, x, y, z, vx, vy, vz):
        # Установка начальных координат и скоростей объекта
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def get_position(self):
        # Возвращает текущие декартовы координаты объекта
        return (self.x, self.y, self.z)

    def update_position(self, t):
        # Обновляет координаты объекта через время t
        self.x += self.vx * t
        self.y += self.vy * t
        self.z += self.vz * t

    def get_spherical_coords(self, radar):
        # Возвращает сферические координаты объекта относительно радара
        return radar.to_spherical(self.x, self.y, self.z)

def main():
    # Создание экземпляра радара
    radar = Radar(0, 0, 0)  # Координаты радара
    n = int(input("Введите количество летающих объектов: "))
    flying_objects = []

    # Ввод данных для каждого летающего объекта
    for i in range(n):
        x, y, z = map(float, input(f"Введите координаты объекта {i+1} (x y z): ").split())
        vx, vy, vz = map(float, input(f"Введите скорости объекта {i+1} (vx vy vz): ").split())
        flying_objects.append(FlyingObject(x, y, z, vx, vy, vz))

    print("\nТекущие сферические координаты объектов относительно радара:")
    # Вывод текущих сферических координат объектов
    for i, obj in enumerate(flying_objects):
        r, azimuth, elevation = obj.get_spherical_coords(radar)
        print(f"Объект {i+1}: r={r:.2f}, азимут={azimuth:.2f}, угол места={elevation:.2f}")

    # Ввод времени для прогноза координат
    t = float(input("\nВведите время в секундах: "))

    print(f"\nСферические координаты объектов относительно радара через {t} секунд:")
    # Обновление и вывод новых сферических координат объектов через заданное время
    for i, obj in enumerate(flying_objects):
        obj.update_position(t)
        r, azimuth, elevation = obj.get_spherical_coords(radar)
        print(f"Объект {i+1}: r={r:.2f}, азимут={azimuth:.2f}, угол места={elevation:.2f}")

if __name__ == "__main__":
    main()