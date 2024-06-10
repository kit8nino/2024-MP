import math
import random

class Radar:
	__instance = None

	def __new__(cls):
		if Radar.__instance is None:
			Radar.__instance = object.__new__(cls)
		return Radar.__instance

		# Модель отправки импульса
	def impulse(self, azimuth, elevation):
		pass

# Класс летающего объекта
class Object:
	def __init__(self, coordinates, velocity):
		self.coordinates = coordinates
		self.velocity = velocity

# Класс координат с возможностью перевода в сферические
class Coordinates:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def to_spherical(self):
		r = math.sqrt(self.x**2 + self.y**2 + self.z**2)
		azimuth = math.degrees(math.atan2(self.y, self.x))
		elevation = math.degrees(math.atan2(self.z, math.sqrt(self.x**2 + self.y**2)))
		return r, azimuth, elevation

# Создание радара
radar = Radar()

# Запрос количества объектов у пользователя
print("Введите количество летающих объектов: ")
objects_amount = int(input())

# Создание списка объектов с автоматическим заполнением данными
objects = []
for i in range(objects_amount):
	cord_x = random.randint(-50, 50)
	cord_y = random.randint(-50, 50)
	cord_z = random.randint(-50, 50)
	speed_x = random.randint(-10, 10)
	speed_y = random.randint(-10, 10)
	speed_z = random.randint(-10, 10)
	objects.append(Object(Coordinates(cord_x, cord_y, cord_z), (speed_x, speed_y, speed_z)))

# Вывод сферических координат объектов, сгенерированных ранее
for object in objects:
	r, azimuth, elevation = object.coordinates.to_spherical()
	print("положение объекта: расстояние -", str(r), ", азимут -", str(azimuth), ", угол возвышения - ", str(elevation))

# Ввод времени с клавиатуры
time = int(input("Введите время в секундах: "))

# Вывод сферических координат объектов через заданное время
for object in objects:
	new_x = object.coordinates.x + object.velocity[0] * time
	new_y = object.coordinates.y + object.velocity[1] * time
	new_z = object.coordinates.z + object.velocity[2] * time
	new_coordinates = Coordinates(new_x, new_y, new_z)
	r, azimuth, elevation = new_coordinates.to_spherical()
	print("положение объекта через", str(time), "секунд : расстояние -", str(r), ", азимут -", str(azimuth), ", угол возвышения - ", str(elevation))