import math

# Класс для радара (Singleton)
class Radar:
    primer = None

    def new(cls):
        if cls.primer is None:
            cls.primer = super(Radar, cls).new(cls)
            cls.primer.coordinates = (0, 0, 0)  # Координаты радара по умолчанию

        return cls.primer

    def set_coordinates(self, x, y, z):
        self.coordinates = (x, y, z)

    def get_coordinates(self):
        return self.coordinates


# Класс для летающих тел
class FlyingTelo:
    def __init__(self, x, y, z, vx, vy, vz):
        self.coordinates = (x, y, z)
        self.skorostes = (vx, vy, vz)

    def new_position(self, t):
        x, y, z = self.coordinates
        vx, vy, vz = self.skorostes

        new_x = x + vx * t
        new_y = y + vy * t
        new_z = z + vz * t

        self.coordinates = (new_x, new_y, new_z)

    def spherical_coordinates(self, radar_coords):
        x, y, z = self.coordinates
        radar_x, radar_y, radar_z = radar_coords

        r = math.sqrt((x - radar_x)**2 + (y - radar_y)**2 + (z - radar_z)**2)
        theta = math.degrees(math.acos((z - radar_z) / r))
        phi = math.degrees(math.atan2(y - radar_y, x - radar_x))

        return r, theta, phi


# Создание радара
radar = Radar()

# Координаты радара
radar.set_coordinates(300, 200, 70)

# 2 летающих тела 
telo1 = FlyingTelo(250, 150, 100, -15, -10, 4)
telo2 = FlyingTelo(200, 150, 700, 8, 2, 9)
arr = [telo1, telo2]

# Вывод текущих сферических координат тел относительно радара
for telo in arr:
    r, theta, phi = telo.spherical_coordinates(radar.get_coordinates())
    print(f"Тело: r = {r}м, θ = {theta}°, φ = {phi}°")
    
# Ввод времени с клавиатуры
t = int(input("Введите время в секундах: "))

# Новое положение тел
for telo in arr:
    telo.new_position(t)

# Вывод новых сферических координат тел относительно радара
for telo in arr:
    r, theta, phi = telo.spherical_coordinates(radar.get_coordinates())
    print(f"Тело через {t} секунд: r = {r}м, θ = {theta}°, φ = {phi}°")